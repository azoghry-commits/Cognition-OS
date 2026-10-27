"""Governed, project-scoped self-improvement records."""

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from .storage import MAX_RECORD_BYTES, read_record


class ImprovementStore:
    STATES = {"OBSERVED", "PROPOSED", "EVALUATED", "APPROVED", "DEPLOYED"}
    WINDOWS_RESERVED_NAMES = {
        "con", "prn", "aux", "nul", "clock$",
        *(f"com{number}" for number in range(1, 10)),
        *(f"lpt{number}" for number in range(1, 10)),
    }

    def __init__(self, workspace):
        self.root = Path(workspace).resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError("Workspace directory required")
        self.project_id = hashlib.sha256(str(self.root).casefold().encode()).hexdigest()[:24]

    def path(self, improvement_id):
        if not isinstance(improvement_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", improvement_id):
            raise ValueError("Invalid improvement id")
        if improvement_id.casefold() in self.WINDOWS_RESERVED_NAMES:
            raise ValueError("Reserved improvement id")
        base = self.root / ".cognition" / "improvements"
        target = base / (improvement_id + ".json")
        if not target.resolve().is_relative_to(self.root):
            raise ValueError("Improvement path escapes project")
        for candidate in [self.root / ".cognition", base, target]:
            if candidate.is_symlink() or (hasattr(candidate, "is_junction") and candidate.is_junction()):
                raise ValueError("Linked improvement paths are forbidden")
        return target

    @staticmethod
    def _required(value, fields):
        if not isinstance(value, dict) or any(value.get(field) in [None, "", [], {}] for field in fields):
            raise ValueError("Missing required improvement fields: " + ", ".join(fields))

    @staticmethod
    def _authorized(authorized):
        if authorized is not True:
            raise ValueError("Explicit improvement persistence authorization required")

    def _read(self, improvement_id):
        record = read_record(self.path(improvement_id))
        if record.get("project_id") != self.project_id or record.get("state") not in self.STATES:
            raise ValueError("Invalid or cross-project improvement record")
        return record

    def _write(self, improvement_id, record):
        encoded = json.dumps(record, ensure_ascii=False, allow_nan=False, indent=2) + "\n"
        if len(encoded.encode("utf-8")) > MAX_RECORD_BYTES:
            raise ValueError("Improvement record exceeds 1 MB")
        path = self.path(improvement_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(".json.tmp")
        if temporary.is_symlink() or (hasattr(temporary, "is_junction") and temporary.is_junction()):
            raise ValueError("Linked temporary improvement paths are forbidden")
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
        temporary.replace(path)
        return {"id": improvement_id, "state": record["state"], "path": str(path), "project_id": self.project_id}

    def observe(self, improvement_id, observation, authorized=False):
        self._authorized(authorized)
        self._required(observation, ["title", "observed_problem", "evidence", "scope"])
        path = self.path(improvement_id)
        if path.exists():
            raise FileExistsError("Improvement record already exists")
        now = datetime.now(timezone.utc).isoformat()
        record = {
            "schema_version": "1.0",
            "project_id": self.project_id,
            "state": "OBSERVED",
            "created_at": now,
            "updated_at": now,
            "observation": observation,
            "history": [{"state": "OBSERVED", "at": now}],
        }
        return self._write(improvement_id, record)

    def propose(self, improvement_id, proposal, authorized=False):
        self._authorized(authorized)
        self._required(proposal, ["change_summary", "rationale", "regression_cases", "rollback_plan"])
        record = self._read(improvement_id)
        if record["state"] != "OBSERVED":
            raise ValueError("Proposal requires an OBSERVED record")
        return self._transition(improvement_id, record, "PROPOSED", "proposal", proposal)

    def evaluate(self, improvement_id, evaluation, authorized=False):
        self._authorized(authorized)
        self._required(evaluation, ["outcome", "evidence", "baseline_results", "candidate_results"])
        if evaluation["outcome"] not in {"PASSED", "FAILED", "INCONCLUSIVE"}:
            raise ValueError("Unknown evaluation outcome")
        record = self._read(improvement_id)
        if record["state"] != "PROPOSED":
            raise ValueError("Evaluation requires a PROPOSED record")
        return self._transition(improvement_id, record, "EVALUATED", "evaluation", evaluation)

    def approve(self, improvement_id, approval, authorized=False):
        self._authorized(authorized)
        self._required(approval, ["approved", "approver", "reason"])
        record = self._read(improvement_id)
        if record["state"] != "EVALUATED" or record["evaluation"]["outcome"] != "PASSED":
            raise ValueError("Approval requires a PASSED evaluation")
        if approval["approved"] is not True:
            raise ValueError("Approval must be explicit")
        return self._transition(improvement_id, record, "APPROVED", "approval", approval)

    def deploy(self, improvement_id, deployment, authorized=False):
        self._authorized(authorized)
        self._required(deployment, ["version", "artifact", "rollback_reference", "verification"])
        record = self._read(improvement_id)
        if record["state"] != "APPROVED":
            raise ValueError("Deployment record requires APPROVED state")
        return self._transition(improvement_id, record, "DEPLOYED", "deployment", deployment)

    def _transition(self, improvement_id, record, state, field, value):
        now = datetime.now(timezone.utc).isoformat()
        record[field] = value
        record["state"] = state
        record["updated_at"] = now
        record["history"].append({"state": state, "at": now})
        return self._write(improvement_id, record)

    def get(self, improvement_id):
        return self._read(improvement_id)

    def list(self, state=None):
        if state is not None and state not in self.STATES:
            raise ValueError("Unknown improvement state")
        base = self.path("probe").parent
        if not base.exists():
            return []
        records = []
        for path in sorted(base.glob("*.json")):
            record = self._read(path.stem)
            if state is None or record["state"] == state:
                records.append({"id": path.stem, "title": record["observation"]["title"], "state": record["state"], "updated_at": record["updated_at"]})
        return records

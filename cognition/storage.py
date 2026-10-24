"""Bounded decoding for untrusted, project-local persistence files."""
import json

MAX_RECORD_BYTES = 1000000


def read_record(path):
    # Bound the actual read, not only a prior stat vulnerable to file growth.
    with path.open('rb') as stream:
        raw = stream.read(MAX_RECORD_BYTES + 1)
    if len(raw) > MAX_RECORD_BYTES:
        raise ValueError('Stored record exceeds 1 MB limit')
    def reject_constant(value):
        raise ValueError('Nonfinite stored JSON value')
    data = json.loads(raw.decode('utf-8'), parse_constant=reject_constant)
    if not isinstance(data, dict):
        raise ValueError('Stored record must be an object')
    return data

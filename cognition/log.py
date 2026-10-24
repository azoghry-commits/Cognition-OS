"""Opt-in JSON diagnostics on stderr; never configures the host root logger."""
import json
import logging
import os
import threading

_LOGGER = logging.getLogger('cognition.operational')
_LOCK = threading.Lock()
_HANDLER: logging.Handler | None = None


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        fields = getattr(record, 'cognition_fields', {})
        return json.dumps({'event': record.getMessage(), 'level': record.levelname, **fields},
                          ensure_ascii=True, allow_nan=False)


def debug(event: str, **fields: str) -> None:
    """Record only allowlisted routing metadata after explicit level opt-in."""
    level = os.environ.get('COGNITION_LOG_LEVEL', '').strip().upper()
    if level != 'DEBUG':
        return
    global _HANDLER
    with _LOCK:
        if _HANDLER is None:
            _HANDLER = logging.StreamHandler()
            _HANDLER.setFormatter(JSONFormatter())
            _LOGGER.addHandler(_HANDLER)
        _LOGGER.setLevel(logging.DEBUG)
        _LOGGER.propagate = False
    safe = {key: value for key, value in fields.items() if key in {'policy', 'resolved_tier'}}
    _LOGGER.debug(event, extra={'cognition_fields': safe})

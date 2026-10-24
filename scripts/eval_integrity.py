"""Finite JSON fingerprints for explicitly reviewed evaluation inputs."""
import hashlib
import json

HASH_SCHEME = 'canonical-json-sha256-v1'


def read_json_bytes(raw):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON object key: ' + key)
            result[key] = value
        return result

    def nonfinite(value):
        raise ValueError('Nonfinite JSON value: ' + value)

    value = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=object_pairs, parse_constant=nonfinite)
    # Also rejects numeric overflow such as 1e999.
    json.dumps(value, allow_nan=False)
    return value


def json_fingerprint(value):
    encoded = json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(encoded.encode('utf-8')).hexdigest()


def review_fingerprints(cases, labels):
    return {'hash_scheme': HASH_SCHEME, 'cases_sha256': json_fingerprint(cases),
            'labels_sha256': json_fingerprint(labels)}


def has_bound_approval(cases, labels, certificate):
    if not isinstance(certificate, dict) or certificate.get('approved') is not True:
        return False
    expected = review_fingerprints(cases, labels)
    return all(certificate.get(key) == value for key, value in expected.items())

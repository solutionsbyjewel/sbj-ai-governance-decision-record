#!/usr/bin/env python3
"""Reference validator for the SBJ V2.0 Decision Record technical release 2.0.0.

Validates JSON Schema structure/cross-field rules and optional externally supplied
conditional-profile activation. Profile IDs are implementation context, not fields in
the Decision Record object.
"""
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

BASE = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((BASE/'schema/sbj-decision-record.schema.json').read_text())
PROFILES = json.loads((BASE/'rules/conditional-profiles.json').read_text())['profiles']

def get_path(obj, path):
    cur = obj
    for part in path.split('.'):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur

def validate(record, activated_profiles):
    errors=[]
    v=Draft202012Validator(SCHEMA, format_checker=FormatChecker())
    for e in sorted(v.iter_errors(record), key=lambda x: list(x.absolute_path)):
        loc='.'.join(str(p) for p in e.absolute_path) or '$'
        errors.append(f'SCHEMA {loc}: {e.message}')
    for pid in activated_profiles:
        if pid not in PROFILES:
            errors.append(f'PROFILE {pid}: unknown profile identifier')
            continue
        for path in PROFILES[pid].get('hard_requirements_when_activated', []):
            if get_path(record, path) is None:
                errors.append(f'PROFILE {pid}: activated profile requires {path}')
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('record', type=Path)
    ap.add_argument('--profiles', default='', help='Comma-separated activated profile IDs, e.g. B,C')
    args=ap.parse_args()
    record=json.loads(args.record.read_text())
    profiles=[x for x in (p.strip() for p in args.profiles.split(',')) if x]
    errors=validate(record, profiles)
    if errors:
        print('FAIL')
        for x in errors: print(' -',x)
        sys.exit(1)
    print('PASS')
if __name__=='__main__': main()

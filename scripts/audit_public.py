#!/usr/bin/env python3
"""Simple audit script to catch obvious secrets or local paths."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
bad = []
for p in ROOT.rglob('*'):
    if p.is_file():
        try:
            txt = p.read_text(errors='ignore')
        except Exception:
            continue
        # skip scanning audit script itself and git/obsidian internal files
        sp = str(p)
        if sp.endswith('scripts/audit_public.py'):
            continue
        if '/.obsidian/' in sp or '/.git/' in sp or '/.githooks/' in sp or '/scripts/' in sp:
            # skip development and local config files
            continue
        if 'BEGIN RSA PRIVATE KEY' in txt or 'PRIVATE KEY' in txt:
            bad.append(f'Possible private key in {p}')
        if '/Users/' in txt:
            bad.append(f'User path in {p}')
if bad:
    print('\n'.join(bad))
    print('audit_public: FAILED')
    sys.exit(2)
print('audit_public: OK')
sys.exit(0)

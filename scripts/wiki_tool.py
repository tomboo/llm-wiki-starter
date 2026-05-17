#!/usr/bin/env python3
"""
Minimal deterministic wiki_tool for the LLM Wiki starter.
Uses only Python standard library.
"""
import argparse
import json
import os
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'Raw' / 'Sources'
WIKI = ROOT / 'Wiki'
SCHEMA = ROOT / 'Schema'
CATALOG = WIKI / 'catalog.jsonl'

ALLOWED_TAGS = {'topic','concept','entity','project','log'}


def read_frontmatter(path: Path):
    data = {'raw': ''}
    if not path.exists():
        return data
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            data['raw'] = fm
            # very small parser for simple YAML lists and scalars
            for line in fm.splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    k,v = line.split(':',1)
                    k=k.strip()
                    v=v.strip()
                    if v.startswith('[') and v.endswith(']'):
                        # inline list (very small parser)
                        items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(',') if x.strip()]
                        data[k]=items
                    elif v in ('true','false'):
                        data[k]= (v=='true')
                    else:
                        data[k]=v.strip().strip('"')
                elif line.startswith('- '):
                    # naive list collector
                    # find last key added that is a list
                    key=None
                    # look backwards
                    for prev in reversed(fm.splitlines()[:fm.splitlines().index(line)]):
                        if ':' in prev:
                            key=prev.split(':',1)[0].strip()
                            break
                    if key:
                        data.setdefault(key,[]).append(line[2:].strip().strip('"'))
    return data


def cmd_doctor(args):
    ok = True
    print('Doctor: checking core folders...')
    for p in ['Raw/Sources','Wiki','Schema','_templates','scripts']:
        if not (ROOT / p).exists():
            print(f'  MISSING: {p}')
            ok=False
        else:
            print(f'  OK: {p}')
    py = sys.version.splitlines()[0]
    print('Python:', py)
    if ok:
        print('Doctor: all basic checks passed')
        return 0
    print('Doctor: issues found')
    return 2


def index_wiki():
    entries=[]
    if not WIKI.exists():
        return entries
    for sub in ['Concepts','Topics','Entities','Projects','Logs']:
        folder = WIKI / sub
        if not folder.exists():
            continue
        for f in folder.glob('*.md'):
            if f.name == 'index.md':
                continue
            if f.name == 'index.md':
                continue
            fm = read_frontmatter(f)
            tag = None
            if 'tags' in fm:
                if isinstance(fm['tags'],list) and fm['tags']:
                    tag = fm['tags'][0]
                else:
                    tag = fm.get('tags')
            title = f.stem
            topics = fm.get('topics', []) or []
            sources = fm.get('sources', []) or []
            updated = datetime.date.fromtimestamp(f.stat().st_mtime).isoformat()
            entries.append({'path':str(f.relative_to(ROOT)),'title':title,'tag':tag or sub[:-1].lower(),'topics':topics,'sources':sources,'updated':updated})
    return entries


def cmd_build(args):
    print('Building catalog and indexes...')
    entries = index_wiki()
    WIKI.mkdir(parents=True, exist_ok=True)
    # write catalog.jsonl
    with open(CATALOG,'w',encoding='utf-8') as fo:
        for e in entries:
            fo.write(json.dumps(e,ensure_ascii=False)+'\n')
    # write top-level index.md
    lines=['# Wiki index','']
    for e in entries:
        lines.append(f"- [{e['title']}]({e['path']}) - {e['tag']}")
    (WIKI / 'index.md').write_text('\n'.join(lines),encoding='utf-8')
    # per-folder indexes
    for sub in ['Concepts','Topics','Entities','Projects','Logs']:
        folder = WIKI / sub
        if not folder.exists():
            continue
        items = list(folder.glob('*.md'))
        lines=[f'# {sub} index','']
        for f in items:
            lines.append(f"- [{f.stem}]({str(f.relative_to(ROOT))})")
        (folder / 'index.md').write_text('\n'.join(lines),encoding='utf-8')
    print('Build complete')
    return 0


def cmd_lint(args):
    print('Running lint on compiled Wiki notes...')
    errors=0
    for sub in ['Concepts','Topics','Entities','Projects','Logs']:
        folder = WIKI / sub
        if not folder.exists():
            continue
        for f in folder.glob('*.md'):
            fm = read_frontmatter(f)
            tags = fm.get('tags',[])
            if isinstance(tags,str):
                tags=[tags]
            if not tags:
                print(f'ERROR {f}: missing tags')
                errors+=1
                continue
            if tags[0] not in ALLOWED_TAGS:
                print(f'ERROR {f}: tag {tags[0]} not allowed')
                errors+=1
            sources = fm.get('sources',[]) or []
            source_count = fm.get('source_count')
            if source_count is not None:
                try:
                    sc = int(source_count)
                except Exception:
                    sc = None
                if sc != len(sources):
                    print(f'ERROR {f}: source_count {source_count} != number of sources {len(sources)}')
                    errors+=1
            # check sources exist
            for s in sources:
                sp = ROOT / s
                if not sp.exists():
                    print(f'ERROR {f}: source {s} does not exist')
                    errors+=1
    if errors:
        print(f'Lint: found {errors} issue(s)')
        return 3
    print('Lint: no issues found')
    return 0


def cmd_source_scan(args):
    print('Scanning Raw/Sources for manifest...')
    SCHEMA.mkdir(parents=True, exist_ok=True)
    manifest = []
    for f in (RAW).glob('*.md'):
        fm = read_frontmatter(f)
        title = fm.get('Title', f.stem)
        processed = fm.get('Processed', False)
        manifest.append({'path':str(f.relative_to(ROOT)),'title':title,'processed':bool(processed),'covered_by':[],'updated':datetime.date.fromtimestamp(f.stat().st_mtime).isoformat()})
    mfpath = SCHEMA / 'source-manifest.jsonl'
    if args.update:
        # attempt to mark processed true if covered by catalog
        covered = {e['path'] for e in index_wiki() for s in e['sources']}
        for m in manifest:
            if m['path'] in covered:
                m['processed']=True
    with open(mfpath,'w',encoding='utf-8') as fo:
        for m in manifest:
            fo.write(json.dumps(m,ensure_ascii=False)+'\n')
    print('Source manifest written to', mfpath)
    return 0


def cmd_source_lint(args):
    print('Running source-lint...')
    mfpath = SCHEMA / 'source-manifest.jsonl'
    issues=0
    if not mfpath.exists():
        print('No source-manifest found; run source-scan --update first?')
        return 4
    manifest = [json.loads(l) for l in mfpath.read_text(encoding='utf-8').splitlines() if l.strip()]
    # build coverage map
    covered = {}
    for e in index_wiki():
        for s in e['sources']:
            covered.setdefault(s,[]).append(e['path'])
    for m in manifest:
        if m.get('processed') and not covered.get(m['path']):
            print('ERROR: source marked processed but has no coverage:', m['path'])
            issues+=1
    if issues:
        print('source-lint: issues found')
        return 5
    print('source-lint: OK')
    return 0


def cmd_search_catalog(args):
    q = args.query.lower()
    if not CATALOG.exists():
        print('No catalog found; run build')
        return 6
    results=[]
    for line in CATALOG.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        if q in e.get('title','').lower() or q in e.get('path','').lower() or q in (e.get('tag') or ''):
            results.append(e)
    for r in results:
        print(json.dumps(r,ensure_ascii=False))
    print(f'Found {len(results)} result(s)')
    return 0


def cmd_log(args):
    title = args.title
    details = args.details
    WIKI.mkdir(parents=True, exist_ok=True)
    logpath = WIKI / 'log.md'
    ts = datetime.datetime.utcnow().isoformat()
    entry = f"- {ts} | {title} | {details}\n"
    with open(logpath,'a',encoding='utf-8') as fo:
        fo.write(entry)
    print('Logged to', logpath)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog='wiki_tool.py')
    sp = p.add_subparsers(dest='cmd')
    sp.add_parser('doctor')
    sp.add_parser('build')
    sp.add_parser('lint')
    ss = sp.add_parser('source-scan')
    ss.add_argument('--update',action='store_true')
    ss.add_argument('--accept-covered',action='store_true')
    sp.add_parser('source-lint')
    sp.add_parser('source-delta')
    sp.add_parser('source-coverage')
    sc = sp.add_parser('search-catalog')
    sc.add_argument('--query',required=True)
    lg = sp.add_parser('log')
    lg.add_argument('--title',required=True)
    lg.add_argument('--details',required=True)
    args = p.parse_args(argv)
    if args.cmd == 'doctor':
        return cmd_doctor(args)
    if args.cmd == 'build':
        return cmd_build(args)
    if args.cmd == 'lint':
        return cmd_lint(args)
    if args.cmd == 'source-scan':
        return cmd_source_scan(args)
    if args.cmd == 'source-lint':
        return cmd_source_lint(args)
    if args.cmd == 'search-catalog':
        return cmd_search_catalog(args)
    if args.cmd == 'log':
        return cmd_log(args)
    print('Unknown command; run with -h for help')
    return 10

if __name__ == '__main__':
    sys.exit(main())

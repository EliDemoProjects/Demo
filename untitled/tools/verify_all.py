import json, os, subprocess, sys
pages = json.load(open('pages.json'))
SRC = [d for d in __import__('glob').glob('/home/claude/sca/*/out/en/')][0]
OUT = '/home/claude/work/out/gitbook-sca/'
ok = 0; bad = {}
for key, (space, fn) in pages.items():
    md = OUT + key
    r = subprocess.run([sys.executable, '/home/claude/skill-update/gitbook-paligo/scripts/verify_text.py', SRC + fn, md,
                        '--includes', OUT + space + '/.gitbook/includes', '--max-diffs', '12'],
                       capture_output=True, text=True)
    if r.returncode == 0: ok += 1
    else: bad[key] = r.stdout
print('identical:', ok, 'of', len(pages))
json.dump(bad, open('verify-bad.json', 'w'), indent=1)
for k, v in bad.items():
    print('=====', k, v.splitlines()[0]); print('\n'.join(v.splitlines()[1:8])[:900])

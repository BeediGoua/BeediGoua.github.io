from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in [root/'index.html',*sorted((root/'projects').glob('*.html'))]:
    text=p.read_text(encoding='utf-8',errors='ignore')
    for href in re.findall(r'href=["\']([^"\']+)',text):
        if href.startswith(('http:','https:','mailto:','#')): continue
        target=(p.parent/href.split('#')[0]).resolve()
        if href and not target.exists(): errors.append(f'{p.relative_to(root)} -> {href}')
    if 'À confirmer' in text or 'TODO' in text: errors.append(f'Placeholder public: {p.relative_to(root)}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('OK: liens locaux et placeholders publics vérifiés')

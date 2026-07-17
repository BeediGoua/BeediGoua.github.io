from pathlib import Path
from bs4 import BeautifulSoup
import subprocess

ROOT = Path(__file__).resolve().parents[1]
html_files = [ROOT/'index.html', ROOT/'index-en.html', *sorted((ROOT/'projects').glob('*.html'))]
errors=[]
for path in html_files:
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    prefix='../' if path.parent.name=='projects' else ''
    script=soup.find('script',src=f'{prefix}assets/js/global-language.js')
    css=soup.find('link',href=f'{prefix}assets/css/global-language.css')
    if not script: errors.append(f'{path.name}: global-language.js absent')
    if not css: errors.append(f'{path.name}: global-language.css absent')
    if not soup.select('[data-set-lang], select[id*="lang" i]'):
        errors.append(f'{path.name}: aucun switch de langue')

for name in ['zimnat.html','music-recommender.html','reviewguardian.html']:
    soup=BeautifulSoup((ROOT/'projects'/name).read_text(encoding='utf-8'),'html.parser')
    if not soup.select('[data-lang="fr"]') or not soup.select('[data-lang="en"]'):
        errors.append(f'{name}: contenu bilingue incomplet')

if errors:
    raise SystemExit('\n'.join(errors))

subprocess.run(['node','--check',str(ROOT/'assets/js/global-language.js')],check=True)
print(f'OK: {len(html_files)} pages, switch global, contenu bilingue et JS valides')

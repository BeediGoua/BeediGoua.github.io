from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json,re
root=Path('/mnt/data/portfolio_langfix/portfolio_work')
files=[root/'index.html',root/'index-en.html']+sorted((root/'projects').glob('*.html'))
fr=json.load(open(root/'assets/lang/fr.json'))
en=json.load(open(root/'assets/lang/en.json'))

def inline_html(path):
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    # strip external styles and scripts, inline local scripts in original order
    for link in soup.find_all('link',href=True):
        link.decompose()
    for script in list(soup.find_all('script',src=True)):
        src=script['src']
        if src.startswith('http'):
            script.decompose(); continue
        target=(path.parent/src).resolve()
        if target.exists():
            new=soup.new_tag('script')
            new.string=target.read_text(encoding='utf-8')
            script.replace_with(new)
        else:
            script.decompose()
    return str(soup)

problems=[]
with sync_playwright() as p:
    br=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    for path in files:
        page=br.new_page(viewport={'width':1440,'height':1000})
        errors=[]
        page.on('pageerror',lambda e: errors.append(str(e)))
        page.set_content(inline_html(path), wait_until='domcontentloaded', timeout=8000)
        page.wait_for_timeout(800)
        if not page.evaluate('!!window.PortfolioLanguage'):
            problems.append((path.name,'global language missing')); page.close(); continue
        for lang,dic in [('en',en),('fr',fr)]:
            page.evaluate("l=>window.PortfolioLanguage.set(l,{navigateHome:false})",lang)
            page.wait_for_timeout(100)
            # wrong language nodes visible?
            wrong='fr' if lang=='en' else 'en'
            visible_wrong=page.locator(f'[data-lang="{wrong}"]:visible').count()
            hidden_right=page.locator(f'[data-lang="{lang}"][hidden]').count()
            if visible_wrong: problems.append((path.name,f'{lang}: {visible_wrong} wrong-language nodes visible'))
            if hidden_right: problems.append((path.name,f'{lang}: {hidden_right} right-language nodes hidden'))
            # i18n text/html exact on representative nodes
            vals=page.locator('[data-i18n]').evaluate_all("els=>els.map(e=>[e.getAttribute('data-i18n'),e.textContent.trim()])")
            for key,text in vals:
                exp=str(dic.get(key,'')).strip()
                # only exact simple strings, skip values containing markup or newlines
                if exp and '<' not in exp and text!=exp:
                    problems.append((path.name,f'{lang}: key {key!r} got {text!r} expected {exp!r}'))
                    break
        # Dynamic education labels
        if path.name in ('index.html','index-en.html'):
            page.evaluate("window.PortfolioLanguage.set('en',{navigateHome:false})")
            page.wait_for_timeout(50)
            labels=page.locator('.education-toggle-label').all_inner_texts()
            if labels and any(x not in ('Details','Collapse') for x in labels): problems.append((path.name,f'education EN labels {labels}'))
            page.evaluate("window.PortfolioLanguage.set('fr',{navigateHome:false})")
            page.wait_for_timeout(50)
            labels=page.locator('.education-toggle-label').all_inner_texts()
            if labels and any(x not in ('Détails','Réduire') for x in labels): problems.append((path.name,f'education FR labels {labels}'))
        # Ignore expected fetch errors; report JS reference errors etc.
        serious=[e for e in errors if 'fetch' not in e.lower() and 'failed to fetch' not in e.lower() and 'localstorage' not in e.lower()]
        if serious: problems.append((path.name,'JS errors: '+repr(serious[:3])))
        page.close()
    br.close()
print('PAGES',len(files),'PROBLEMS',len(problems))
for p in problems[:200]: print(' -',p)
if problems: raise SystemExit(1)

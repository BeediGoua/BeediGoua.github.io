# Global language QA

- Shared language state: `portfolioLanguage` (legacy key `lang` mirrored)
- Query-string fallback: `?lang=fr` / `?lang=en`
- Static home variants synchronized: `index.html` / `index-en.html`
- All internal HTML links receive the active language
- CV download follows the active language
- Every detail page exposes a language switch (existing or injected)
- Legacy additional-project pages now contain French and English content

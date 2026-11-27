# Python cheat sheet

My working reference for the Lexicon Python course: Python basics, classes, SQLite, MongoDB/PyMongo, APIs (requests + FastAPI), pandas, dates and charts. It opens with a "Things I often miss" box.

## Open it

Double-click `python-cheat-sheet.html` (or drag it into a browser). It works offline: hover code to see explanations, click to pin, and use the search box at the top.

## How it is built

- `source/original.html` – my original sheet (sections 01–38 and the glossary).
- `build/content.py` – the added sections, the "Things I often miss" list and glossary terms.
- `build/build.py` – adds everything to the original and writes the finished page.

Rebuild after changing `content.py`:

```bash
cd "00. Cheat Sheet"
python3 -I build/build.py "$PWD/build" source/original.html python-cheat-sheet.html
```

Examples use a made-up library/books dataset so they don't give away lab answers.

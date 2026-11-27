import ast, html, re, sys
sys.path.insert(0, sys.argv[1])
from content import SECTIONS, GLOSSARY, LINKS, MISS

src, out = sys.argv[2], sys.argv[3]
s = open(src).read()

KW = set("from import for in if def return class raise None True False and or not else elif while with as is lambda pass".split())

HELP = {
  "MongoClient": "Connect to a MongoDB server. client[\"name\"] picks a database; db[\"name\"] picks a collection.",
  "pprint": "Pretty-print: shows a long dict or nested document over several readable lines.",
  "list_collection_names": "List the names of every collection in this database.",
  "find": "find(filter, projection): returns a cursor of matching documents. Loop over it. No filter = every document.",
  "find_one": "find_one(filter, projection): returns ONE dict, or None if nothing matches. Don't loop over it.",
  "count_documents": "count_documents(filter): returns an int. The filter is required; {} counts every document. No projection here.",
  "distinct": "distinct(\"field\"): a list of every different value that field has in the collection.",
  "keys": "dict.keys(): the key names of one dict, here the field names of one document.",
  "insert_one": "insert_one(doc): add one document. Returns a result object; read .inserted_id from it.",
  "insert_many": "insert_many([doc, doc]): add a list of documents. Returns a result object with .inserted_ids.",
  "inserted_id": "The _id of the document insert_one just added. Read it from the result; no need to search.",
  "inserted_ids": "List of _id values insert_many just added.",
  "update_one": "update_one(filter, change): change the first match. The change dict must use an operator such as $set.",
  "update_many": "update_many(filter, change): change every match. Returns ONE result object, not documents.",
  "delete_one": "delete_one(filter): remove the first matching document.",
  "delete_many": "delete_many(filter): remove every matching document. Count with the same filter first.",
  "matched_count": "How many documents the filter matched.",
  "modified_count": "How many documents actually changed (a $set to the same value counts as matched, not modified).",
  "deleted_count": "How many documents were removed.",
  "upsert": "upsert=True: if nothing matches, insert a new document built from the filter and the change.",
  "sort": "sort(\"field\", 1) ascending or sort(\"field\", -1) descending. Chained onto find().",
  "limit": "limit(n): return at most n documents.",
  "skip": "skip(n): leave out the first n documents (after sorting).",
  "dict.get": "dict.get(\"key\", default): the value, or the default (None if not given) when the key is missing. No KeyError.",
  "datetime": "A date-and-time object from the datetime module. Compare dates as datetime objects (not strings) and turn them into text with strftime.",
  "connect": "sqlite3.connect(\"file.db\"): open (or create) a database file and return a connection.",
  "execute": "Run one SQL statement. Put ? where values go and pass the values as a tuple.",
  "fetchall": "Get all result rows as a list of tuples.",
  "commit": "Save INSERT / UPDATE / DELETE changes to the file. Reading with SELECT doesn't need it.",
  "requests.get": "Send an HTTP GET request. Returns a Response object: check .status_code, read .json().",
  "requests.post": "Send an HTTP POST request, usually with json= for the body.",
  "getenv": "os.getenv(\"NAME\"): read an environment variable (e.g. loaded from .env). Returns None if it is not set.",
  "status_code": "The HTTP status number: 200 OK, 201 Created, 404 Not Found, 422 bad data, 500 server bug.",
  "r.json": "Parse the response's JSON text into Python lists and dicts. A method: needs ().",
  "params=": "Query parameters: requests adds them to the URL as ?key=value.",
  "json=": "Body data: requests turns the dict into JSON and sends it in the request body.",
  "headers=": "Extra request headers, such as an API key.",
  "timeout=": "Seconds to wait before giving up.",
  "FastAPI": "Create the app object. Routes are registered on it with @app.get, @app.post …",
  "BaseModel": "Pydantic base class. A subclass describes the JSON body: field names and types. Wrong data → 422.",
  "HTTPException": "raise HTTPException(status_code=…, detail=…) stops the route and sends that error to the client.",
  "app.get": "Route decorator: the function below answers GET requests to this path.",
  "app.post": "Route decorator: the function below answers POST requests (create).",
  "app.put": "Route decorator: the function below answers PUT requests (replace every field).",
  "app.patch": "Route decorator: the function below answers PATCH requests (change some fields).",
  "app.delete": "Route decorator: the function below answers DELETE requests.",
  "status_code=": "The status code sent on success: 201 for created, 204 for deleted with no body.",
  "model_dump": "Turn a Pydantic object into a normal dict.",
  "exclude_unset=": "Keep only the fields the client actually sent. The key to PATCH.",
  "detail=": "The error message sent to the client in the JSON body.",
  "default=": "Value max() returns when the sequence is empty, so the first id becomes 1.",
  "update": "dict.update(other): copy every key/value from other into this dict, overwriting matches.",
}
STR_HELP = {
  "$gt": "Greater than: {\"year\": {\"$gt\": 1950}} is year > 1950.",
  "$gte": "Greater than or equal: >=.",
  "$lt": "Less than: <.",
  "$lte": "Less than or equal: <=.",
  "$ne": "Not equal: !=.",
  "$in": "Value is one of a list, like SQL IN.",
  "$exists": "The field is there (True) or missing (False).",
  "$or": "At least one of the listed filters matches. Sits at the top level and takes a list.",
  "$set": "Update operator: set a field to a value (creates it if missing).",
  "$inc": "Update operator: add to a number. Use a negative number to subtract.",
  "$push": "Update operator: append to a list, even if the value is already there.",
  "$addToSet": "Update operator: append to a list only if the value isn't there yet.",
  "$unset": "Update operator: remove a field. The value (\"\") is ignored.",
  "_id": "Every document's unique key. \"_id\": 0 in a projection hides it.",
}

TOK = re.compile(r'(?P<c>#[^\n]*)|(?P<s>[fbr]?"(?:[^"\\\n]|\\.)*"|[fbr]?\'(?:[^\'\\\n]|\\.)*\')|(?P<n>\b\d+(?:\.\d+)?\b)|(?P<i>[A-Za-z_]\w*)|(?P<o>.|\n)')

def tip(cls, text, help_):
    c = f"{cls} explain".strip()
    return f'<span class="{c}" tabindex="0" data-help="{html.escape(help_)}">{text}</span>'

def hl(code):
    out, prev_ident, prev_dot = [], None, False
    toks = list(TOK.finditer(code))
    for k, m in enumerate(toks):
        t = m.group(0); e = html.escape(t, quote=True)
        if m.group("c"):
            out.append(f'<span class="comment">{e}</span>')
        elif m.group("s"):
            inner = t.strip('fbr')[1:-1]
            out.append(tip("string", e, STR_HELP[inner]) if inner in STR_HELP else f'<span class="string">{e}</span>')
        elif m.group("n"):
            out.append(f'<span class="number">{e}</span>')
        elif m.group("i"):
            nxt = code[m.end():m.end()+2]
            key = None
            if t in KW:
                out.append(f'<span class="keyword">{e}</span>')
            else:
                if nxt[:1] == "=" and nxt != "==" and f"{t}=" in HELP: key = f"{t}="
                elif prev_dot and prev_ident and f"{prev_ident}.{t}" in HELP: key = f"{prev_ident}.{t}"
                elif t == "get" and prev_dot: key = "dict.get"
                elif t == "update" and prev_ident == "existing": key = "update"
                elif t in HELP and t not in ("update", "json"): key = t
                out.append(tip("", e, HELP[key]) if key else e)
            prev_ident = t; prev_dot = False; continue
        else:
            out.append(e)
            if t == ".": prev_dot = True; continue
        prev_ident = None if not (m.group("o") and t == ".") else prev_ident
        prev_dot = False
    return "".join(out)

start_num = len(re.findall(r'<h2><span>\d+</span>', s)) + 1
secs = []
for n, sec in enumerate(SECTIONS, start_num):
    ast.parse(sec["code"])  # syntax check every example
    notes = "".join(f"<p>{html.escape(p, quote=False)}</p>" for p in sec["notes"])
    links = " · ".join(f'<a href="{u}" style="color:var(--blue)">{html.escape(t)} ↗</a>' for u, t in sec["links"])
    if links: notes += f"<p>{links}</p>"
    secs.append(f'<section><h2><span>{n}</span>{sec["title"]}</h2><pre><code>{hl(sec["code"])}</code></pre>{notes}</section>')
marker = '</div><div id="glossary"'
assert s.count(marker) == 1
s = s.replace(marker, "\n" + "\n".join(secs) + "\n" + marker)

groups = []
for g, terms in GLOSSARY.items():
    btns = []
    for term, alt, help_ in terms:
        gname = html.unescape(g).lower()
        search = f"{gname} {term.lower()} {alt.lower()} {help_.lower()}"
        btns.append(f'<button type="button" class="explain glossary-term" data-help="{html.escape(help_)}" data-search="{html.escape(search)}">{html.escape(term)}</button>')
    groups.append(f'<div class="glossary-group"><h3>{g}</h3><div class="glossary-terms">{"".join(btns)}</div></div>')
gl_end = '</div></div><p class="glossary-intro">Reference links:'
assert s.count(gl_end) == 1
s = s.replace(gl_end, "</div>" + "".join(groups) + '</div><p class="glossary-intro">Reference links:')
s = s.replace('<a href="https://git-scm.com/docs/git">Git</a>', '<a href="https://git-scm.com/docs/git">Git</a> · ' + " · ".join(f'<a href="{u}">{t}</a>' for u, t in LINKS))

n_sec = len(re.findall(r'<h2><span>\d+</span>', s))
n_terms = s.count('class="explain glossary-term"')
s = re.sub(r'\d+ sections · \d+ glossary terms', f'{n_sec} sections · {n_terms} glossary terms', s)
s = re.sub(r'Glossary · \d+ terms', f'Glossary · {n_terms} terms', s)
s = s.replace("PYTHON / WORKING REFERENCE / 24 SEP 2026", "PYTHON / WORKING REFERENCE / 27 NOV 2026")
s = s.replace("Values → collections → loops → functions → unpacking → objects.", "Values → collections → loops → functions → unpacking → objects → SQL → MongoDB → APIs → pandas → charts.")
s = s.replace("Try: return, slicing, **kwargs…", "Try: return, **kwargs, $set, groupby, strftime…")

# "Things I often miss" block at the top of the page
mark = {"bad": "✗ ", "good": "✓ "}
items = []
for rule, parts in MISS:
    chips = " ".join(f'<code class="{k}">{mark[k]}{html.escape(c)}</code>' if k else f'<span class="aside">{html.escape(c)}</span>' for k, c in parts)
    items.append(f"<li><span class=\"rule\">{html.escape(rule)}</span>{chips}</li>")
miss = ('<section id="often-missed" class="miss"><div class="eyebrow">CHECK THESE FIRST</div>'
        '<h2>Things I often miss</h2><ol>' + "".join(items) + '</ol></section>')
css = ('.miss{border:1px solid var(--line);border-radius:6px;padding:16px 22px 8px;margin-bottom:30px}.miss h2{margin:4px 0 12px}'
       '.miss ol{margin:0;padding-left:22px;columns:2;column-gap:40px}.miss li{break-inside:avoid;margin:0 0 12px;font-size:12px;line-height:1.6}'
       '.miss .rule{display:block}.miss code{font:inherit;white-space:pre-wrap;margin-right:10px;display:inline-block}'
       '.miss code.bad{color:var(--ochre)}.miss code.good{color:var(--green)}.miss .aside{color:var(--muted)}'
       '@media(max-width:1180px){.miss ol{columns:1}}@media print{.miss{break-inside:avoid}}')
assert s.count("</style>") >= 1 and s.count("</header>") == 1
s = s.replace("</style>", css + "</style>", 1)
s = s.replace("</header>", "</header>" + miss, 1)
s = s.replace('<nav class="reference-nav" aria-label="Jump to">', '<nav class="reference-nav" aria-label="Jump to"><a href="#often-missed">Often missed ↓</a>', 1)

open(out, "w").write(s)
print(n_sec, n_terms, len(s))

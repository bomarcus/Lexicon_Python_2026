SECTIONS = []

def S(title, code, notes, links=(), lang="python"):
    SECTIONS.append(dict(title=title, code=code.strip("\n"), notes=notes, links=links, lang=lang))

PM = "https://www.mongodb.com/docs/languages/python/pymongo-driver/current/"
FA = "https://fastapi.tiangolo.com/tutorial/"

S("MongoDB · connect &amp; look around", '''
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]             # database
books = db["books"]                # collection, same as db.books

db.list_collection_names()         # which collections exist?
pprint(books.find_one())           # what does one document look like?
books.find_one().keys()            # just the field names
books.count_documents({})          # how many documents in total?
books.distinct("genre")            # every value one field has
''', ["Look before you query. Field names and values are case-sensitive: \"Genre\" is not \"genre\", \"Göteborg\" is not \"goteborg\". A typo raises no error, you just get nothing back. In VS Code, select one line and press Shift+Enter to run only that line."],
  [(PM + "connect/", "PyMongo: connect"), (PM, "PyMongo guide"), ("https://pymongo.readthedocs.io/en/stable/api/", "API reference")])

S("find, find_one &amp; count", '''
# find(filter) → a cursor: loop over it, each document is a dict
for book in books.find({"genre": "Fantasy"}):
    print(book["title"], book["year"])

# Several keys in one filter = AND
books.find({"genre": "Fantasy", "in_stock": True})

# find_one(filter) → ONE dict, or None if nothing matches
book = books.find_one({"title": "Dune"})
if book:
    print(book["author"])          # read it, don't loop over it

# count_documents(filter) → an int.  {} = every document
n = books.count_documents({"genre": "Sci-fi"})
all_books = list(books.find())     # cursor → list
''', ["find gives many documents, so you loop. find_one gives one dict, so a for loop over it walks its keys, not documents. count_documents always needs a filter; {} means all. A filter is always key: value pairs, so {\"_id\"} (a set) is not a filter."],
  [(PM + "crud/query/find/", "Find documents"), (PM + "crud/query/count/", "Count documents")])

S("Query operators", '''
# SQL                        MongoDB filter
# year > 1950                {"year": {"$gt": 1950}}
# year >= 1950               {"year": {"$gte": 1950}}
# year < 1950                {"year": {"$lt": 1950}}
# year <= 1950               {"year": {"$lte": 1950}}
# genre != 'Horror'          {"genre": {"$ne": "Horror"}}
# genre IN ('A', 'B')        {"genre": {"$in": ["A", "B"]}}
# isbn IS NOT NULL           {"isbn": {"$exists": True}}

# Range: two operators on the same field
books.find({"pages": {"$gte": 200, "$lte": 400}})

# OR: a list of complete filters
books.find({"$or": [{"genre": "Poetry"}, {"pages": {"$lt": 100}}]})

# Dates: compare with datetime objects, not strings
from datetime import datetime
books.find({"added": {"$lt": datetime(2026, 1, 1)}})
''', ["The operator goes inside the field's value: {field: {\"$op\": value}}. $or is the exception: it sits at the top and takes a list of filters."],
  [(PM + "crud/query/specify-query/", "Specify a query")])

S("Filter vs projection: two dicts", '''
for book in books.find(
    {"genre": "Fantasy"},                 # 1st = FILTER:     which documents?
    {"title": 1, "year": 1, "_id": 0},    # 2nd = PROJECTION: which fields?
):
    print(book)       # {'title': ..., 'year': ...}  (no _id)

books.find({}, {"_id": 0})                # every doc, every field except _id
''', ["Filter ≈ WHERE, projection ≈ the columns after SELECT. Projection: all 1s = only these fields, all 0s = everything except these; don't mix (only \"_id\": 0 may join the 1s). A value like \"Fantasy\" never goes in the projection, and 1 in a filter means \"equals the number 1\".",
   "The second dict means something different per method: projection in find/find_one, the change ($set …) in update_one/update_many. count_documents takes only a filter."],
  [(PM + "crud/query/project/", "Specify fields to return")])

S("Arrays &amp; nested documents", '''
# One document:
# {"title": "Dune", "tags": ["classic", "space"],
#  "publisher": {"name": "Chilton", "city": "Philadelphia"},
#  "reviews": [{"user": "kim", "stars": 5}, {"user": "lee", "stars": 3}]}

# In a FILTER, dot notation reaches inside
books.find({"tags": "classic"})                 # list contains "classic"
books.find({"publisher.city": "Philadelphia"})  # nested dict
books.find({"reviews.stars": 5})                # any review with 5 stars

# In PYTHON: one [ ] per level, and loop over lists
book = books.find_one({"title": "Dune"})
print(book["publisher"]["city"])
print(len(book["reviews"]))                     # how many in the list
for review in book["reviews"]:
    print(review["user"], review["stars"])
''', ["\"publisher.city\" is only understood by MongoDB, inside a filter or projection. In Python, book[\"publisher.city\"] is a KeyError: write book[\"publisher\"][\"city\"]. A list of dicts needs a loop, then [ ] on each item."],
  [(PM + "crud/query/specify-query/", "Query nested fields")])

S("Sort, limit &amp; safe reads", '''
books.find().sort("year", -1).limit(3)             # -1 = descending, 1 = ascending
books.find().sort("title", 1).skip(10).limit(10)   # skip 10, show the next 10

book.get("isbn")                  # None if the field is missing
book.get("isbn", "no isbn")       # your default if missing
book["isbn"]                      # KeyError if missing
''', ["get belongs to the dict: book.get(\"field\", default). The thing before the dot is the object you ask; the field name goes inside the parentheses. Documents in one collection don't all need the same fields, so .get is safer for optional ones."],
  [(PM + "crud/query/specify-documents-to-return/", "Sort, limit, skip")])

S("Insert &amp; result objects", '''
result = books.insert_one({"title": "Emma", "author": "Austen"})
print(result.inserted_id)          # the new ObjectId(...), no search needed

result = books.insert_many([
    {"_id": 501, "title": "Persuasion"},
    {"_id": 502, "title": "Mansfield Park"},
])
print(result.inserted_ids)         # [501, 502]
''', ["Write methods return a result object, not documents. Read the answer from it: inserted_id, inserted_ids, matched_count, modified_count, deleted_count. Inserting an _id that already exists raises DuplicateKeyError. Without your own _id, MongoDB creates an ObjectId."],
  [(PM + "crud/insert/", "Insert documents")])

S("Update operators", '''
f = {"title": "Emma"}                                    # which documents?
books.update_one(f, {"$set": {"year": 1815}})            # set a field
books.update_one(f, {"$inc": {"copies": -1}})            # add / subtract
books.update_one(f, {"$push": {"tags": "romance"}})      # append (duplicates ok)
books.update_one(f, {"$addToSet": {"tags": "romance"}})  # append only if missing
books.update_one(f, {"$unset": {"isbn": ""}})            # remove a field

result = books.update_many({"genre": "Poetry"}, {"$set": {"shelf": "P"}})
print(result.matched_count, result.modified_count)

# upsert: no match → insert a whole new document
books.update_one({"title": "Beowulf"}, {"$set": {"year": 1000}}, upsert=True)
''', ["update_one(filter, change). The change must use an operator: a plain {\"year\": 1815} raises an error. update_many returns one result object, so don't loop over it. upsert creates a new document when nothing matches; it does not add items to a list (that's $push / $addToSet)."],
  [(PM + "crud/update/", "Update documents"), ("https://www.mongodb.com/docs/manual/reference/operator/update/", "Update operators")])

S("Delete &amp; the dry run", '''
f = {"copies": 0}                       # ONE shared filter variable

print(books.count_documents(f))         # 1. how many would be hit?
for book in books.find(f, {"title": 1}):
    print(book)                         # 2. look at them

result = books.delete_many(f)           # 3. same filter, for real
print(result.deleted_count)             # 4. matches step 1?

books.delete_one({"_id": 501})
''', ["Use the same pattern before update_many: count, look, write, then compare matched_count / modified_count with your count. Messed up the test data? Re-run the seed script to start clean."],
  [(PM + "crud/delete/", "Delete documents")])

S("Same question: SQL · sqlite3 · PyMongo", '''
# SQL in DB Browser
#   SELECT title FROM books WHERE genre = 'Fantasy' AND year > 1950;

# sqlite3 in Python: ? placeholders + a tuple of values
import sqlite3
conn = sqlite3.connect("library.db")
cur = conn.execute(
    "SELECT title FROM books WHERE genre = ? AND year > ?",
    ("Fantasy", 1950),
)
for row in cur.fetchall():
    print(row[0])                  # each row is a tuple
conn.commit()                      # only after INSERT / UPDATE / DELETE
conn.close()

# PyMongo: the values go straight into the filter dict
for book in db.books.find({"genre": "Fantasy", "year": {"$gt": 1950}},
                          {"title": 1, "_id": 0}):
    print(book["title"])           # each document is a dict
''', ["Same filter, three spellings. SQL: AND and > in text. sqlite3: one ? per value, values in a tuple (one value still needs a comma: (\"Fantasy\",)). PyMongo: several keys = AND, > becomes {\"$gt\": …}, no placeholders."],
  [("https://docs.python.org/3/library/sqlite3.html", "sqlite3 docs")])

S("requests: call an API", '''
import requests

BASE = "http://127.0.0.1:8000"

# GET with query parameters: requests builds ?author=Austen
r = requests.get(f"{BASE}/books", params={"author": "Austen"}, timeout=5)
print(r.status_code)               # check this first: 200?
if r.status_code == 200:
    data = r.json()                # JSON text → Python list / dict

# POST: send data in the body with json=
new_book = {"title": "Emma", "author": "Austen", "year": 1815}
r = requests.post(f"{BASE}/books", json=new_book, timeout=5)
print(r.status_code, r.json())     # 201 {...}

# A header, e.g. an API key
r = requests.get(f"{BASE}/books", headers={"X-API-Key": "your-key"}, timeout=5)

# Nested JSON: one [ ] per level, like a Mongo document
# data["results"][0]["title"]
''', ["params= goes in the URL (filters). json= goes in the body (data you send). r.json() is a method call, so it needs the parentheses."],
  [("https://requests.readthedocs.io/en/latest/user/quickstart/", "requests quickstart")])

S("API docs notation → Python", '''
# What a lab sheet or API docs write:
#   GET https://api.example.com/users/<username>/books
#   params:  sort=added, per_page=5
#   header:  Authorization: Bearer <token>
# <...> is a placeholder: replace it with a real value

import os
import requests

username = "anna"
url = f"https://api.example.com/users/{username}/books"  # <username> → {username}

token = os.getenv("BOOKS_TOKEN")      # "BOOKS_TOKEN" = the name in .env
                                      # token = your Python variable
headers = {"Authorization": f"Bearer {token}"}   # header line → dict
params = {"sort": "added", "per_page": 5}        # each key=value → dict entry

r = requests.get(url, params=params, headers=headers, timeout=5)
books = r.json()

# A helper like get_json(url, params=..., headers=...) takes the same pieces
''', ["Read the docs line by line: the method picks requests.get / post, the URL becomes an f-string with your values in { }, every params line becomes one key in a dict, every header line becomes one key in another dict. The token comes from .env via os.getenv (load it with python-dotenv's load_dotenv() first), so it never sits in your code or on GitHub.",
   "Don't write the literal word <username> or <token> in the URL; the angle brackets mean \"your value goes here\"."],
  [("https://requests.readthedocs.io/en/latest/user/quickstart/", "Requests quickstart"),
   ("https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview", "MDN: HTTP overview"),
   ("https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user", "GitHub: list repos for a user")])

S("FastAPI: app &amp; running it", '''
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Hobbit", "author": "Tolkien", "year": 1937},
]

@app.get("/books")                 # method + path
def list_books():
    return books                   # list / dict → JSON automatically

# Terminal 1:  fastapi dev main.py         (leave it running)
# Browser:     http://127.0.0.1:8000/docs  (try every route)
# Terminal 2:  python3 client.py           (the + in VS Code)
''', ["Saving main.py restarts the server, and a plain Python list starts over. Connection refused means the server in terminal 1 isn't running (Ctrl+C stopped it). Two routes with the same method and path: only the first runs, so change the existing function instead of adding another."],
  [(FA + "first-steps/", "FastAPI first steps")])

S("Path &amp; query parameters", '''
# Path parameter: /books/3   ({ } in the route)
@app.get("/books/{book_id}")
def get_book(book_id: int):            # "abc" → 422 automatically
    return find_book(book_id)

# Query parameters: /books?author=tolkien&year=1937
@app.get("/books")
def search_books(author: str | None = None, year: int | None = None):
    result = books                     # start with everything
    if author:
        result = [b for b in result if author.lower() in b["author"].lower()]
    if year:
        result = [b for b in result if b["year"] == year]
    return result                      # the filtered list, not books
''', ["A name in { } in the route is a path parameter; every other function parameter is a query parameter. str | None = None: type str or None, default None. Without = None it's required. Inside a function, only use names from its def line or ones you created there."],
  [(FA + "path-params/", "Path parameters"), (FA + "query-params/", "Query parameters")])

S("Body: POST, PUT, PATCH, DELETE", '''
class Book(BaseModel):                 # every field required (POST, PUT)
    title: str
    author: str
    year: int

class BookUpdate(BaseModel):           # every field optional (PATCH)
    title: str | None = None
    author: str | None = None
    year: int | None = None

def find_book(book_id: int):           # plain helper, no @app line
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@app.post("/books", status_code=201)
def create_book(book: Book):
    new_id = max((b["id"] for b in books), default=0) + 1
    new_book = {"id": new_id, **book.model_dump()}
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}")           # replace every field
def replace_book(book_id: int, updated: Book):
    existing = find_book(book_id)
    existing["title"] = updated.title  # dict uses [ ], Pydantic object uses .
    existing["author"] = updated.author
    existing["year"] = updated.year
    return existing

@app.patch("/books/{book_id}")         # change only the fields sent
def patch_book(book_id: int, changes: BookUpdate):
    existing = find_book(book_id)
    existing.update(changes.model_dump(exclude_unset=True))
    return existing

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    existing = find_book(book_id)
    books.remove(existing)             # 204 = no body, nothing to return
''', ["A Pydantic class describes the body the client sends; query parameters never need one. model_dump() turns it into a normal dict; exclude_unset=True keeps only the fields the client actually sent. Close the path string before the next argument: \"/books/{book_id}\", status_code=204."],
  [(FA + "body/", "Request body"), (FA + "body-updates/", "PUT vs PATCH"), (FA + "handling-errors/", "Handling errors")])

S("Status codes &amp; errors", '''
# 200 OK             a normal GET, PUT or PATCH
# 201 Created        @app.post(..., status_code=201)
# 204 No Content     @app.delete(..., status_code=204), return nothing
# 401 Unauthorized   missing or wrong API key
# 404 Not Found      raise HTTPException(status_code=404, ...)
# 422 Unprocessable  wrong type or missing field in body / parameters
# 500 Server error   a bug in your route

raise HTTPException(status_code=404, detail="book not found")

# What a 422 looks like:
# {"detail": [{"loc": ["body", "year"], "msg": "Field required", ...}]}
#   loc = where the problem is, msg = what's wrong
''', ["On a 500, read the traceback in the server terminal from the bottom up: the last line says what went wrong, the line above points into your file. A 422 after copying code often means old field names in the body."],
  [(FA + "handling-errors/", "Handling errors")])

PD = "https://pandas.pydata.org/docs/"

S("pandas · load &amp; look", '''
import pandas as pd

books = pd.read_csv("data/books.csv")      # path from the notebook's folder

books.head()                  # first 5 rows (books.tail() = last 5)
books.shape                   # (rows, columns), no ( ) after shape
books.info()                  # columns, types, non-null counts (prints, returns None)
books.describe()              # count, mean, min, max … of number columns
books.columns                 # column names
books["genre"].unique()       # every different value
books["genre"].value_counts() # how many of each value
books.isna().sum()            # missing values per column
books["title"].count()        # non-missing values (len(books) counts all rows)
''', ["shape is (rows, columns). info() prints by itself, so display(books.info()) shows an extra None. count() vs len() is a quick way to spot a missing value.",
      "Run All stops at the first error cell, so every cell below it never runs. Comment out cells that fail on purpose, and after a kernel restart re-run from the top (Restart → Run All)."],
  [(PD + "user_guide/10min.html", "10 minutes to pandas"), (PD + "reference/api/pandas.read_csv.html", "read_csv")])

S("Select columns &amp; rows", '''
books["title"]                     # one column → Series
books[["title", "year"]]           # several → DataFrame (a list inside [ ])
cols = ["title", "year"]
books[cols]                        # cols is already a list: single [ ]

books.loc[3, "title"]              # by index LABEL and column name
books.iloc[0]                      # by POSITION: first row
books.iloc[-1]                     # last row
books.iloc[:5, :2]                 # first 5 rows, first 2 columns

# Filter rows with a mask: ( ) around EVERY comparison next to & or |
old_fantasy = books[(books["genre"] == "Fantasy") & (books["year"] < 1950)]
books[(books["genre"] == "Poetry") | (books["pages"] < 100)]
books[~books["genre"].isin(["Horror", "Crime"])]    # ~ = not
books[books["year"].between(1900, 1999)]            # both ends included
books.loc[books["pages"] > 500, ["title", "pages"]] # rows + columns at once
''', ["Only the column name goes inside the quotes: books[\"year\"] < 1950, never books[\"year < 1950\"]. A True/False column is already a mask: loans[loans[\"returned\"]]. & runs before ==, so a comparison without its own ( ) gives a wrong count instead of an error."],
  [(PD + "user_guide/indexing.html", "Indexing and selecting"), (PD + "reference/api/pandas.Series.between.html", "Series.between")])

S("Clean &amp; save it back", '''
# Each method returns a NEW object: chain the steps, then save it back
books["genre"] = books["genre"].str.strip().str.lower()

price_clean = books["price"].str.replace(" kr", "")   # part of the text
price_clean = price_clean.str.replace(",", ".")       # build on price_clean
books["price"] = price_clean.astype(float)            # save into the table

books["genre"] = books["genre"].replace({"sci fi": "sci-fi"})  # whole values

books = books.drop_duplicates()            # drop on the TABLE, save back
books = books.dropna(subset=["title"])     # drop rows missing a title
books["genre"] = books["genre"].fillna("unknown")
books = books.drop(columns=["notes"])

# where keeps values where True; mask replaces values where True
books["pages"] = books["pages"].mask(books["pages"] == 0)   # 0 → NaN
books["year"] = books["year"].where(books["year"].between(1450, 2026))
''', ["Left side of = decides what you overwrite: books[\"price\"] = … changes one column, books = … replaces the whole table. .str.replace changes part of a text; .replace({…}) swaps whole values. Running a cleaning line without saving it changes nothing."],
  [(PD + "user_guide/text.html", "Working with text"), (PD + "user_guide/missing_data.html", "Missing data"), (PD + "reference/api/pandas.DataFrame.mask.html", "DataFrame.mask")])

S("New columns", '''
import numpy as np

books["decade"] = books["year"] // 10 * 10
books["price_per_page"] = books["price"] / books["pages"]

# np.where(condition, value_if_true, value_if_false): ONE call
books["length"] = np.where(books["pages"] > 400, "long", "short")

# pd.cut: numbers → labelled bins, saved in a NEW column
books["age_group"] = pd.cut(
    books["year"],
    bins=[0, 1900, 1990, 2026],
    labels=["classic", "modern", "recent"],
)
''', ["New columns go on the left with a new name, so the source column stays intact for checks. Test the source column, not the label you just made."],
  [("https://numpy.org/doc/stable/reference/generated/numpy.where.html", "np.where"), (PD + "reference/api/pandas.cut.html", "pd.cut")])

S("groupby, sort &amp; merge", '''
# One number per group
books.groupby("genre")["pages"].mean()
books.groupby("genre")["pages"].agg(["count", "median", "mean"])
books.groupby("genre")["price"].median().sort_values(ascending=False)

# Sort: column first, keywords after
books.sort_values("year", ascending=False).head(10)
books["decade"].value_counts().sort_index()   # counts in decade order

# merge: add columns from a second table; how="left" keeps every book
genres = pd.read_csv("data/genre_groups.csv")
print(len(books))
books = books.merge(genres, on="genre", how="left")
print(len(books))                             # same count? no duplicates
books["genre_group"].isna().sum()             # books with no match
''', ["value_counts counts rows; an average per group needs groupby. Positional arguments come first, keyword arguments after, and no extra ( ) around them: sort_values(\"pages\", ascending=False). Check the row count before and after every merge: more rows means the key isn't unique in the second table."],
  [(PD + "user_guide/groupby.html", "Group by"), (PD + "user_guide/merging.html", "Merge, join, concatenate")])

S("Dates in pandas", '''
# Text → datetime. format must match the text exactly
books["added"] = pd.to_datetime(books["added"], format="%b %d %Y", errors="coerce")
books["added"].isna().sum()      # NaT = could not be parsed

from pandas.tseries.api import guess_datetime_format
guess_datetime_format("Jun 12 1998")   # '%b %d %Y'

books["added"].dt.year                       # .dt opens date parts
books["added"].dt.month_name()
books["added"].dt.strftime("%m-%d").value_counts().head()   # top days

too_late = books["added"] > pd.Timestamp("2011-12-31")
books.loc[too_late, "added"] = books.loc[too_late, "added"] - pd.DateOffset(years=100)

books[books["added"].between("1990-01-01", "1999-12-31")]
''', ["pd.to_datetime is a pandas function that takes the column: pd.to_datetime(books[\"added\"]), not books[\"added\"].pd.to_datetime(). errors=\"coerce\" turns bad values into NaT instead of crashing, so count NaT afterwards. .dt only works after the column is a datetime; after a kernel restart re-run the convert cell."],
  [(PD + "reference/api/pandas.to_datetime.html", "pd.to_datetime"), (PD + "user_guide/timeseries.html", "Time series"), (PD + "reference/api/pandas.DateOffset.html", "DateOffset")])

S("strftime codes", '''
from datetime import datetime

d = datetime(1998, 6, 12, 14, 5)

# %Y 1998   year, 4 digits       %y 98     year, 2 digits
# %m 06     month number         %b Jun    month, short name
# %B June   month, full name     %d 12     day of month
# %a Fri    weekday, short       %A Friday weekday, full
# %H 14     hour, 24h            %M 05     minute
# %j 163    day of the year

print(d.strftime("%Y-%m-%d"))      # 1998-06-12   date → text
print(d.strftime("%d %b %Y"))      # 12 Jun 1998
datetime.strptime("Jun 12 1998", "%b %d %Y")   # text → date
''', ["The same codes work in strftime (date → text), strptime and pd.to_datetime(format=…) (text → date). Spaces, dashes and commas in the format must match the text."],
  [("https://docs.python.org/3/library/datetime.html#format-codes", "Format codes")])

S("matplotlib · one chart", '''
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(figsize=(8, 4))

counts = books["decade"].value_counts().sort_index()
ax.plot(counts.index, counts.values, marker="o")      # line
# ax.bar(x, heights)   ax.hist(values, bins=20)   ax.scatter(x, y)

ax.set_title("Books per decade")
ax.set_xlabel("Decade")
ax.set_ylabel("Number of books")
ax.xaxis.set_major_locator(MultipleLocator(10))       # a tick every 10
# ax.set_xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

median = counts.median()
ax.axhline(median, color="grey", linestyle="--", label=f"median {median:.0f}")
# ax.axvline(1945, color="black", label="1945")       # vertical line
ax.legend()                                           # shows the labels
plt.show()
''', ["Every chart needs a title, axis labels and one sentence in markdown about what it shows. value_counts sorts by count; add .sort_index() before a line chart so x runs in order. A label= only appears once you call ax.legend()."],
  [("https://matplotlib.org/stable/users/explain/quick_start.html", "matplotlib quick start"), ("https://matplotlib.org/stable/api/ticker_api.html", "Tick locators")])

S("seaborn", '''
import seaborn as sns

sns.set_theme()                       # nicer default style, once

fig, ax = plt.subplots()
sns.histplot(data=books, x="pages", bins=30, ax=ax)
ax.set_title("Pages per book")
plt.show()

fig, ax = plt.subplots()
sns.boxplot(data=books, x="genre", y="pages", ax=ax)    # spread + outliers
plt.show()

fig, ax = plt.subplots()
sns.barplot(data=books, x="genre", y="price", estimator="median", ax=ax)
plt.show()

fig, ax = plt.subplots()
sns.scatterplot(data=books, x="pages", y="price", hue="genre", ax=ax)
plt.show()

sns.countplot(data=books, x="genre")  # counts rows per value
''', ["seaborn takes the whole table as data= and column NAMES as text. Pass ax=ax to draw into your own figure, then style it with the same ax.set_… calls as matplotlib. Skewed numbers: compare median and mean and look at the boxplot for outliers."],
  [("https://seaborn.pydata.org/tutorial/function_overview.html", "seaborn overview"), ("https://seaborn.pydata.org/api.html", "seaborn API")])

S("Notebook output tricks", '''
from IPython.display import display

display(books.head(), books.shape)     # several outputs from one cell

genres = ["Fantasy", "Poetry", "Crime"]
print(*genres, sep="\\n")               # one per line, no brackets

for i, genre in enumerate(genres, start=1):
    print(f"{i:02}. {genre}")          # 01. Fantasy  02. Poetry …

print(f"{1234567.891:,.2f}")           # 1,234,567.89
print(f"{0.4567:.1%}")                 # 45.7%

top = books.sort_values("pages").head(3)   # save on its own line …
display(top)                               # … then display it
''', ["Only the last line of a cell is shown automatically; use display() for more. Assign on its own line, never inside display(…). Keyword arguments like sep= go straight into print( ), not in extra parentheses."],
  [("https://docs.python.org/3/library/string.html#format-specification-mini-language", "Format spec"), ("https://docs.python.org/3/library/functions.html#enumerate", "enumerate")])

S("Common mistakes · check these first", '''
# ✗ {"_id"}                         a set, not a filter
f = {"_id": 501}                    # ✓ key: value.   {} = every document

# ✗ for k in books.find_one(f):     loops over the KEYS of one dict
book = books.find_one(f)            # ✓ one dict: read book["title"]

# ✗ book{"title"}                   dict values use [ ]
title = book["title"]               # ✓  (a Pydantic object uses .title)

# ✗ book["publisher.city"]          dot paths work in filters only
city = book["publisher"]["city"]    # ✓ one [ ] per level

# ✗ city.get(...)                   ask the dict, not the value
city = book.get("city", "unknown")  # ✓

# ✗ for r in books.update_many(...):   it's ONE result object
result = books.update_many(f, {"$set": {"shelf": "A"}})
print(result.modified_count)        # ✓ also result.inserted_id

# ✗ books.find_one(f, {"$addToSet": ...})   operators go in update_*
# ✗ books.count_documents(f, {"title": 1})  count takes a filter only

# ✗ return outside a function → use print()
# ✗ for book in books          → missing ":" at the end
# ✗ return movie   (def line says updated)  → only names you have
''', ["Collected from questions that came up more than once. Before writing code, read the exercise twice and check which field it asks you to match on, for example an id rather than a name or a quantity."])

GLOSSARY = {
  "MongoDB": [
    ("collection", "", "A group of documents in a MongoDB database, like a table in SQL. db[\"books\"] or db.books."),
    ("document", "doc", "One record in a collection, like a row. In Python it arrives as a dict, and it can hold lists and nested dicts."),
    ("cursor", "", "What find() returns: a lazy sequence of documents. Loop over it, or wrap it in list(). It is not a list and not one document."),
    ("filter", "query", "The dict that picks which documents match: {\"genre\": \"Fantasy\"}. {} matches every document. Always key: value pairs."),
    ("projection", "", "The second dict in find/find_one that picks which fields come back: {\"title\": 1, \"_id\": 0}. Like the columns after SELECT."),
    ("_id", "objectid", "Every document's unique key. MongoDB creates an ObjectId if you don't give one. Inserting a duplicate raises DuplicateKeyError."),
    ("ObjectId", "", "MongoDB's generated id type, shown as ObjectId('…'). Read the new one from result.inserted_id after insert_one."),
    ("query operator", "$gt $gte $lt $lte $ne $in $exists $or", "A $ word inside a filter: {\"year\": {\"$gt\": 1950}} means year > 1950. $or takes a list of filters."),
    ("update operator", "$set $inc $push $addtoset $unset", "A $ word in the second dict of update_one/update_many that says how to change: $set, $inc, $push, $addToSet, $unset."),
    ("upsert", "", "update_one(..., upsert=True): update a match, or insert a whole new document when nothing matches. It does not add items to a list."),
    ("dot notation", "nested field", "\"publisher.city\" reaches into a nested dict or a list of dicts, but only inside a filter or projection. In Python use doc[\"publisher\"][\"city\"]."),
    ("result object", "inserted_id matched_count modified_count deleted_count", "What write methods return: InsertOneResult, UpdateResult, DeleteResult. Read inserted_id, matched_count, modified_count or deleted_count from it."),
    ("MongoClient", "pymongo", "The PyMongo connection: MongoClient(\"mongodb://localhost:27017/\"). client[\"name\"] picks a database."),
  ],
  "pandas &amp; charts": [
    ("DataFrame", "df table", "A pandas table: rows and named columns. books[\"title\"] picks one column (a Series)."),
    ("Series", "column", "One column of a DataFrame: values plus an index. Most column methods (.str, .dt, .mean()) work on a Series."),
    ("index", "loc iloc", "The row labels of a DataFrame. .loc uses labels, .iloc uses positions (0 = first row)."),
    ("mask", "boolean filter", "A True/False Series used to pick rows: books[books[\"year\"] < 1950]. Combine with &, |, ~ and ( ) around each comparison."),
    ("NaN", "missing value na null", "Not a Number: pandas' missing value. isna().sum() counts them; dropna() removes rows, fillna() fills them."),
    ("NaT", "not a time", "Not a Time: a missing date. pd.to_datetime(..., errors=\"coerce\") turns text it can't read into NaT."),
    ("dtype", "type str int64 float64 datetime64", "The data type of a column: int64, float64, str, datetime64, category. Check with info() or .dtypes."),
    ("method chaining", "chain", "Calling methods one after another: books[\"genre\"].str.strip().str.lower(). Read left to right; each step works on the previous result."),
    ("groupby", "aggregate agg", "Split rows into groups by a column, then calculate one value per group: books.groupby(\"genre\")[\"pages\"].mean()."),
    ("merge", "join how left", "Add columns from another table where a key matches. how=\"left\" keeps every row of the left table. Check row counts before and after."),
    ("outlier", "skew median mean", "A value far from the rest. Outliers pull the mean but barely move the median; a boxplot shows them as dots."),
    ("figure &amp; axes", "fig ax subplots", "fig, ax = plt.subplots(): fig is the whole image, ax is one chart inside it. Titles, labels and lines go on ax."),
    ("legend", "label", "The box naming each line or colour. Give plot calls a label=, then call ax.legend()."),
    ("strftime", "strptime format codes", "Turn a date into text with codes like %Y-%m-%d. strptime / pd.to_datetime(format=…) go the other way, text to date."),
  ],
  "APIs &amp; FastAPI": [
    ("API", "web api", "A program's interface for other programs. A web API answers HTTP requests, usually with JSON."),
    ("HTTP method", "get post put patch delete verb", "What a request wants to do: GET reads, POST creates, PUT replaces, PATCH changes some fields, DELETE removes."),
    ("route", "endpoint path", "A method plus a path that a function answers, set by a decorator like @app.get(\"/books\")."),
    ("decorator", "@app.get", "The @ line above a function. @app.get(\"/books\") registers the function under it as the handler for that route."),
    ("path parameter", "", "A value inside the URL path, named with { } in the route: /books/{book_id}. It must also be a function parameter."),
    ("query parameter", "params", "A value after ? in the URL: /books?author=Austen. In FastAPI, any function parameter not in the path. In requests, pass params={…}."),
    ("request body", "body json=", "Data sent inside a POST/PUT/PATCH request, usually JSON. In requests, json={…}; in FastAPI, a Pydantic model parameter."),
    ("Pydantic model", "basemodel model_dump exclude_unset", "A class inheriting BaseModel that describes and validates a body. model_dump() gives a dict; exclude_unset=True keeps only sent fields."),
    ("JSON", "r.json()", "Text format for data that looks like Python dicts and lists. r.json() turns a response into Python objects."),
    ("status code", "200 201 204 404 422 500", "The number that says how a request went: 2xx OK, 4xx the client's fault (404 not found, 422 bad data), 5xx a bug on the server."),
    ("HTTPException", "", "raise HTTPException(status_code=404, detail=\"…\") stops the route and sends that status and message to the client."),
    ("header", "x-api-key", "Extra information sent with a request, such as an API key: headers={\"X-API-Key\": key}."),
    ("timeout", "", "requests.get(..., timeout=5): give up after 5 seconds instead of waiting forever."),
    ("/docs", "swagger", "FastAPI's automatic test page at http://127.0.0.1:8000/docs. Try every route from the browser."),
    ("fastapi dev", "uvicorn server", "The terminal command that starts your FastAPI server and restarts it when you save. Leave it running in its own terminal."),
  ],
}

LINKS = [("https://pymongo.readthedocs.io/en/stable/", "PyMongo"), ("https://www.mongodb.com/docs/manual/", "MongoDB manual"),
         ("https://fastapi.tiangolo.com/tutorial/", "FastAPI tutorial"), ("https://requests.readthedocs.io/en/latest/", "requests"),
         ("https://pandas.pydata.org/docs/", "pandas"), ("https://matplotlib.org/stable/", "matplotlib"), ("https://seaborn.pydata.org/", "seaborn")]

# "Things I often miss": shown at the TOP of the page, most frequent first.
# Each item: (rule, [(kind, code)]) where kind is "bad", "good" or "" (plain text)
MISS = [
  ("Inside a function, only use names from its def line or ones you created there.",
   [("bad", 'def get_book(book_id): url = f"{BASE}/books/{id}"'), ("good", '{book_id}'), ("", "id is a built-in, not your variable")]),
  ("f-strings need the f, the variable (not a string) in { }, and the whole lookup inside the braces.",
   [("bad", '"Book {book_id}"'), ("good", 'f"Book {book_id}"'), ("bad", "{'book_id'}"), ("good", "{book_id}"), ("bad", "f\"{book}['title']\""), ("good", "f\"{book['title']}\"")]),
  ("Curly braces outside an f-string make a set or a dict.",
   [("bad", 'input({f"Title: "})'), ("good", 'input(f"Title: ")'), ("bad", '{"_id"}'), ("good", '{"_id": 501}'), ("bad", 'params={"q": {title}}'), ("good", 'params={"q": title}')]),
  ("A trailing comma makes a tuple. len() of it is 1.",
   [("bad", 'late = (books[books["year"] > 2011],)'), ("good", 'late = books[books["year"] > 2011]')]),
  ("Methods return a NEW object: save it back, and the left side of = decides what you overwrite.",
   [("bad", 'books["title"].str.strip()'), ("good", 'books["title"] = books["title"].str.strip()'), ("bad", 'books = pd.to_datetime(books["added"])'), ("good", 'books["added"] = pd.to_datetime(books["added"])')]),
  ("Each step builds on the previous result, not on the original column.",
   [("bad", 'clean = books["price"].str.replace(",", ".")'), ("good", 'clean = clean.str.replace(",", ".")'), ("", "after clean = books[\"price\"].str.replace(\" kr\", \"\")")]),
  ("Masks: only the column name goes in quotes, and every comparison next to & or | gets its own ( ).",
   [("bad", 'books["year < 1950"]'), ("bad", 'books["genre"] == "Poetry" & books["year"] < 1950'), ("good", '(books["genre"] == "Poetry") & (books["year"] < 1950)')]),
  ("Positional arguments first, keyword arguments after, no extra ( ). Assign on its own line, then display.",
   [("bad", 'sort_values((ascending=False), "year")'), ("good", 'sort_values("year", ascending=False)'), ("bad", "display(top = books.head())"), ("good", "top = books.head()"), ("good", "display(top)")]),
  ("pd.function(column) vs column.method(): to_datetime belongs to pd.",
   [("bad", 'books["added"].pd.to_datetime()'), ("good", 'pd.to_datetime(books["added"], format="%b %d %Y")')]),
  ("Run All stops at the first error. After a restart, run from the top; comment out cells that fail on purpose.",
   [("", "AttributeError: .dt → the convert cell didn't run")]),
  ("The name in quotes comes from .env; the name before = is your variable. Read it once in config.py, store it, import it.",
   [("good", 'API_KEY = os.getenv("API_KEY")'), ("good", "from config import API_KEY")]),
  ("API key vs token: an API key from .env goes in X-API-Key; a JWT from /login goes in Authorization: Bearer. Build headers inside the function that has the token.",
   [("good", 'headers={"X-API-Key": API_KEY}'), ("good", 'headers={"Authorization": f"Bearer {token}"}')]),
  ("Copying a template (a teammate's function): same shape, your own URL, dict keys and headers.",
   [("bad", 'data["member_id"]'), ("good", 'data["book_id"]'), ("", "in a books function")]),
  ("Write is not (not just not); else never takes a condition (use elif).",
   [("bad", "if book not None:"), ("good", "if book is not None:"), ("bad", "else book:"), ("good", "else:")]),
  ("int(input()) crashes when the user just presses Enter: read the text first, convert only if it isn't empty.",
   [("bad", 'int(input("Year: ")) or None'), ("good", 'text = input("Year: ")'), ("good", "year = int(text) if text else None")]),
  ("A 204 response has no body, so don't call .json() on it. Read JSON only when there is one (e.g. an error).",
   [("bad", "r = requests.delete(url); r.json()"), ("good", "if r.status_code != 204: print(r.json())")]),
  ("Git: first push sets the upstream; fix an unpushed message with --amend; in Vim press Esc then :wq; after git switch reopen open files in VS Code so an old buffer isn't saved onto the new branch; branches start with feature/ (singular).",
   [("good", "git push -u origin feature/book-search"), ("good", 'git commit --amend -m "Add book search"'), ("good", ":wq")]),
]

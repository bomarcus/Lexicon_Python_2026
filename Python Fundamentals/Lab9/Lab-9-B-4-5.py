# Lab-9_B-4

# Create several PDFDocument and TextDocument objects and store them in one list.
# Loop through the list and print each document's title and the result of describe().
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return (f" {self.title} - description")


class PDFDocument(Document):
    def describe(self):
        return (f" {self.title} - pdf-description")


class TextDocument(Document):
    def describe(self):
        return (f" {self.title} - txt-description")


docs = [
    PDFDocument("HP1"),
    PDFDocument("HP2"),
    TextDocument("HP3"),
    TextDocument("HP3")
]

for doc in docs:
    print(doc.describe())

# Lab-9_B-2-3

# Create PDFDocument(Document) and TextDocument(Document).
# Override describe() in both subclasses so they return different descriptions.
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return (f" {self.title} description")


class PDFDocument(Document):
    def describe(self):
        return (f" {self.title} pdf-description")


class TextDocument(Document):
    def describe(self):
        return (f" {self.title} txt-description")

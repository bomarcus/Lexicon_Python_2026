# Lab-9_B-1

# Create a base class Document with a title attribute and a method describe().

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return (f" {self.title} description")



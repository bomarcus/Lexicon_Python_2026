# Lab-9_C-1-5

# Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
# Give both classes a method called display_status().
# Create objects from both classes and store them in the same list.
# Loop through the list and call display_status) on each object.

class Printer:
    def __init__(self, name):
        self.name = name

    def display_status(self):
        return (f" {self.name} - display status")


class Screen:
    def __init__(self, name):
        self.name = name

    def display_status(self):
        return (f" {self.name} - screen status")


printers_and_screens = [
    Printer("p1"),
    Printer("p2"),
    Screen("s1"),
    Screen("s2")
]

for thing in printers_and_screens:
    print(thing.display_status())

#  5. In a comment, explain why this works even though the classes do not share a base class.
# Every object has display_status()

# Lab-8_A-1

# Create a BadTeam class with name and a default parameter members=[]. Add an add_member() method.

class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, name):
        self.members.append(name)


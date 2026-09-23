# Lab-8_A-2

# Create a BadTeam class with name and a default parameter members=[]. Add an add_member() method.

class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, name):
        self.members.append(name)

team1 = BadTeam("bad team 1")
team2 = BadTeam("bad team 2")

team1.add_member("first")

print(team1.name)
print(team1.members)
print(team2.name)
print(team2.members)

# all instances share the empty default list, so addition to team1 will also show up in team2
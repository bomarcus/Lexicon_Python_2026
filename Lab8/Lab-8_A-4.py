# Lab-8_A-4

# Create a corrected Team class using None as the default value and create a new list inside _init_.

class Team:
    def __init__(self, name, members = None):
        self.name = name
        
        # if members are None -> create empty list.
        if members is None:
            members =[]

        self.members = members

    def add_member(self, name):
        self.members.append(name)

team1 = Team("bad team 1")
team2 = Team("bad team 2")

team1.add_member("first member")
team2.add_member("second member")

print(team1.name, team1.members)
print(team2.name, team2.members)


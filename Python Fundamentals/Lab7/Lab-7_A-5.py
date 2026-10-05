# Lab-7_A-5

# Create one object using keyword arguments.

class Horse:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

horse1 = Horse(color="brown", breed="shetland")
horse2 = Horse(color="white", breed="donkey")

print(horse1.color, horse1.breed)
print(horse2.color, horse2.breed)
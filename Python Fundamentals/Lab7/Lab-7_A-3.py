# Lab-7_A-3
# Create two objects with the same attribute values.
# Use is to check whether they are the same object.


class Horse:
    def __init__(self, color):
        self.color = color

horse1 = Horse("Brown")
horse2 = Horse("Brown")

print(horse1 is horse2)

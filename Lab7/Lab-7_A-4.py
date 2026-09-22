# Lab-7_A-4
# Add a default value to at least one _init_ parameter.

class Clothes:
    def __init__(self, shirt, pants="blue"):
        self.shirt = shirt
        self.pants = pants

clothes1 = Clothes("green", "black")
clothes2 = Clothes("green")

print(clothes1.shirt)
print(clothes1.pants)
print(clothes2.shirt)
print(clothes2.pants)
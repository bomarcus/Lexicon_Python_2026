# Lab-2_C-3

fruits = {
    "kiwi",
    "banana",
    "pear",
    "orange"
}
print(fruits)

# add
fruits.add("dragon fruit")
print("added dragon fruit to set", fruits)

# remove
fruits.remove("orange")
print("removed orange from set", fruits)
fruits.discard("pear")
print("discarded pear from set", fruits)

# membership testing
print("is kiwi in fruits?", "kiwi" in fruits, fruits)

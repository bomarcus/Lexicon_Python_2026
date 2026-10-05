# Lab-3_C-5

# count how many words in a list has more than 5 characters.
names =  [
    "dan",
    "johan",
    "marcus",
    "jocke",
    "viking",
    "eva",
    "Michaela"
]
long_names = 0
for name in names:
    if len(name) > 5:
        long_names += 1
print(long_names)
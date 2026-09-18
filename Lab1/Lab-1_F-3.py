# Lab-1_F-3

word = "foundation"

# display first two and last two chars of word replacing all else with "*"
first_2 = slice(0, 2)
last_2 = slice(-2, None)
star_numbers = len(word) - 4
stars = star_numbers * "*"

print(f"{word[first_2]}{stars}{word[last_2]}")

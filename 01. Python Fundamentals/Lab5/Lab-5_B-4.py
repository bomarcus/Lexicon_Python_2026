# Lab-5_B-4

# Write build _sentence(separator, *words) returning one joined string.

words = ("one", "fine", "day")
separator = (" ")


def build_sentence(separator, *words):
    sentence = separator.join(words)
    return sentence


print(build_sentence(separator, *words))

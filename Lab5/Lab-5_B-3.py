# Lab-5_B-3

# Write longest_word(*words) returning the longest word.
words = [
    "apple",
    "banana",
    "cherry",
    "locomotive",
    "encyclopedia",
]


def longest_word(*words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(longest_word(*words))

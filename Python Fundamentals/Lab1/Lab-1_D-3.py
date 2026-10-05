# Lab-1_D-3

# .split(), .strip(), .replace(), in operator.

sentence = "   a bunch  _   of words  ."

# print original string.
print(sentence)

# return list of words in string.  
print(sentence.split())

# return copy of string. removes matching chars from start/end one by one.
print(sentence.strip(". _ocabunhf"))

# return copy of string with first argument replaced by second.
print(sentence.replace("words", "cats"))

if "bunch" in sentence:
    print("the word 'bunch' is in sentence")

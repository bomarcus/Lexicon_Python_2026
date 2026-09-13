# Lab-3_B-2

# ask for a language
# check if answer is present in a predefined list of supported languages.

# create a list of languages.
supported_languages =[
    "swedish",
    "finnish",
    "english",
    "swahili",
    "mandarin",
    "japanese"
]
# ask for language input from user
user_input = input("Input Language: ")
#check if language input by user is in supported_languages list and print results.
if user_input in supported_languages:
        print("language supported!")
else:
        print("language not supported.")

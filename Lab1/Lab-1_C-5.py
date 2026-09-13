# Lab-1_C-5

# extract username and domain separately from an emailadress using string operations.
email = "altavista@gmail.com"
#find @
at_sign = email.find("@")
print(f"username is {email[0:at_sign]}")
print(f"domain is {email[at_sign+1:]}")

# replace word Java with Python in sentece. print both original and changed.
sentence_java = "Java is great"
sentence_python = sentence_java.replace("Java", "Python")
print(sentence_java)
print(sentence_python)
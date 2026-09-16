# Lab-1_C-5

# extract username and domain separately from an emailadress using string operations.
email = "altavista@gmail.com"
#find @
at_sign = email.find("@")
print(f"username is {email[0:at_sign]}")
print(f"domain is {email[at_sign+1:]}")
# Lab-5_D-1
# Write show_profile(**info) and iterate over all key/value pairs.

info = {
    "first_name": "Marcus",
    "last_name": "Ohlsson",
    "city": "Stockholm",
    "course": "Python",
    "active": True
}


def show_profile(**info):
    for key, value in info.items():
        print(key, ":", value)


show_profile(**info)

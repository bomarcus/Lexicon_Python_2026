# Lab-3_C-7

# loop over a dictionary using keys, values and .items() i three different examples.
# create dict
names =  {
    "player_1": {
        "player_name": "Dan",
        "player_score": 30
        },
    "player_2": {
        "player_name": "Jan",
        "player_score": 120
        },
    "player_3":{
        "player_name": "Bo",
        "player_score": 50
        }
}

for key in names:
    print(key)

for value in names.values():
    print(value)

for key, value in names.items():
    print(value["player_name"], value["player_score"])

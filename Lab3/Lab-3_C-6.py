# Lab-3_C-6

# given a list of scores. count passes and fails using 70 as threshold.

scoreboard = [
    50,
    30,
    70,
    100,
    20,
    10,
    10
]
#create variables for pass and fail.
passes = (0)
fails = (0)
# for score 

# if score in list is 70 or above. add 1 to passes. if not add 1 to fails.
for score in scoreboard:
    if score >= 70:
        passes += 1
    else:
        fails += 1

print(f"passes: {passes}. fails: {fails}.")

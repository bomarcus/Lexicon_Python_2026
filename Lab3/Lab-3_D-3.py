# Lab-3_D-3

# use enumerate to create a playlist with track numbers.

track_list = (
    "John Riley",
    "Pretty Peggy",
    "Geordie",
    "Hush Little Baby",
    "Donna Donna"
)

for index, value in enumerate(track_list, 1):
    print(index, value)

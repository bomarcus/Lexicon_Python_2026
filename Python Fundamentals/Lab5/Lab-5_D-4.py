# Lab-5_D-4

# Write a function that accepts ** settings and returns only settings whose value is not None.

settings = {
    "setting1": "Max",
    "setting2": "Low",
    "setting3": None,
    "setting4": "Medium"
}


def input_settings(**settings):
    has_values = {}
    for key, value in settings.items():
        if value is not None:
            has_values[key] = value
    return has_values


print(input_settings(**settings))

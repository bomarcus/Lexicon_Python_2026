import subprocess

from animals import animals


# MENU PRINT
# print menu
def menu_print(menu, show_numbers=True, show_back=True):
    subprocess.run(["clear"], check=False)
    print(
        f"-------------------------\n       {menu['title']}\n-------------------------"
    )
    # convert to list and slice away first item
    for key, value in menu["options"].items():
        if show_numbers:
            print(f"{key} - {value}")
        else:
            print(value)
    print("-------------------------")
    if show_back:
        print("Press Enter to return to main menu")
        print("-------------------------")


# MAIN MENU
def show_main_menu(player):
    menu_print(main_menu, show_back=False)

    choice = input("pick number: ")

    if choice == "1":
        return feeding_schedule
    elif choice == "2":
        return food_storage
    elif choice == "3":
        return visit_animals
    elif choice == "4":
        return show_inventory
    return show_main_menu


main_menu = {
    "title": "MAIN MENU",
    "options": {
        "1": "Check Feeding Schedule",
        "2": "Go to Food Storage",
        "3": "Visit Animals",
        "4": "Show inventory",
    },
}


# FEEDING SCHEDULE
def feeding_schedule(player):

    for key, animal in animals.items():
        animal_name = animals_menu["options"][key]

        breakfast_check = "[ ]"
        dinner_check = "[ ]"

        if animal.isfed_breakfast:
            if animal.breakfast_points == 1:
                breakfast_check = "[+1]"
            else:
                breakfast_check = "[-1]"

        if animal.isfed_dinner:
            if animal.dinner_points == 1:
                dinner_check = "[+1]"
            else:
                dinner_check = "[-1]"

        feeding_schedule_menu["options"][key] = (
            f"{animal_name} - {animal.feed} - "
            f"Breakfast {breakfast_check} - Dinner {dinner_check}"
        )
    menu_print(feeding_schedule_menu, show_numbers=False)
    input("")
    return show_main_menu


feeding_schedule_menu = {
    "title": "FEEDING SCHEDULE",
    "options": {"1": "Cow", "2": "Tiger", "3": "Elephant"},
}


# FOOD STORAGE
def food_storage(player):
    menu_print(food_storage_menu)
    choice = input("pick number: ")

    if choice == "":
        return show_main_menu

    if choice not in food_storage_menu["options"]:
        return food_storage

    selected_food = food_storage_menu["options"][choice]

    if player.inventory is not None:
        print("Replace", player.inventory, "with", selected_food, "?")
        food_replace = input("yes or no: ")

        if food_replace != "yes":
            return food_storage

    player.pick_up_food(selected_food)
    input(f" you picked up {selected_food}. Press enter to return to menu ")

    return show_main_menu


food_storage_menu = {
    "title": "FOOD STORAGE INVENTORY",
    "options": {
        "1": "Hay",
        "2": "Meat",
        "3": "Fruit",
    },
}


# VISIT ANMIMALS
def visit_animals(player):
    menu_print(animals_menu)
    choice = input("pick number: ")

    if choice == "":
        return show_main_menu

    if choice not in animals:
        return visit_animals

    animal = animals[choice]
    animal_name = animals_menu["options"][choice]

    if animal.isfed_breakfast and animal.isfed_dinner:
        input(f"{animal_name} is full!")
        return visit_animals

    if player.inventory is None:
        input("You have no food. Press Enter to continue ")
        return visit_animals

    give_food = input(f" Give {player.inventory} to {animal_name}? yes or no? ")

    if give_food != "yes":
        return visit_animals

    if player.inventory != animal.feed:
        give_food_anyway = input(
            f" {animal_name} does not like this food.  Give anyway? yes or no? "
        )
        if give_food_anyway != "yes":
            return visit_animals

    food_accepted = animal.give_food(player.inventory)

    if food_accepted:
        if player.inventory == animal.feed:
            print(f"{animal_name} loves it! ")
        else:
            print(f"{animal_name} disliked it. ")

        player.inventory = None

    input("press Enter to continue ")
    return show_main_menu


animals_menu = {
    "title": "ANIMAL PEN",
    "options": {"1": "Cow", "2": "Tiger", "3": "Elephant"},
}


# INVENTORY
# show player inventory
def show_inventory(player):
    inventory_menu = {"title": "INVENTORY", "options": {}}

    if not player.inventory:
        inventory_menu["options"]["1"] = "Inventory empty."
    else:
        inventory_menu["options"]["1"] = f"You are carrying {player.inventory}."

    menu_print(inventory_menu, show_numbers=False)
    input("")
    return show_main_menu

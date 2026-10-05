import subprocess

from animals import animals
from menus import (
    show_main_menu,
)
from zookeeper import Zookeeper

# its morning at the zoo! give the animals food!


# GAME LOOP
def game_loop():
    subprocess.run(["clear"], check=False)
    print("It's a new day at the zoo!")
    print("Feed each animal breakfast and dinner.")
    print("Food they like earns +1 point. Food they dislike earns -1.")
    print("Give it your all, to keep away from Arbetsförmedlingen!")
    print("Have fun!")
    input("Press Enter to start\n")

    player = Zookeeper()
    current_menu_state = show_main_menu

    while True:
        current_menu_state = current_menu_state(player)

        day_done = True

        for animal in animals.values():
            if not animal.isfed_breakfast or not animal.isfed_dinner:
                day_done = False

        if day_done:
            subprocess.run(["clear"], check=False)
            print("All animals have eaten. The day is done!")
            input("press Enter to get your score for the day. Fingers crossed!")
            break


game_loop()

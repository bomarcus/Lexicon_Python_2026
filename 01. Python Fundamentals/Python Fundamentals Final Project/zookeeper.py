class Zookeeper:
    def __init__(self, inventory=None):
        self.inventory = inventory

    def pick_up_food(self, food):
        self.inventory = food

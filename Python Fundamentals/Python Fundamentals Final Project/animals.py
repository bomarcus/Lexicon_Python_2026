class Animal:
    def __init__(self, feed) -> None:
        self.feed = feed
        self.isfed_breakfast = False
        self.isfed_dinner = False

        self.breakfast_points = 0
        self.dinner_points = 0

    def give_food(self, food):
        if not self.isfed_breakfast:
            if food == self.feed:
                self.breakfast_points = 1
            else:
                self.breakfast_points = -1

            self.isfed_breakfast = True
            return True

        elif not self.isfed_dinner:
            if food == self.feed:
                self.dinner_points = 1
            else:
                self.dinner_points = -1

            self.isfed_dinner = True
            return True

        return False


class Cow(Animal):
    def __init__(self):
        super().__init__("Hay")


class Tiger(Animal):
    def __init__(self):
        super().__init__("Meat")


class Elephant(Animal):
    def __init__(self):
        super().__init__("Fruit")


animals = {
    "1": Cow(),
    "2": Tiger(),
    "3": Elephant(),
}

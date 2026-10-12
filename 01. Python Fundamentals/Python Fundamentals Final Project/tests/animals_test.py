from animals import Animal, Cow, Tiger, Elephant


def test_animal():
    animal = Animal("test_food")

    assert animal.feed == "test_food"
    assert animal.isfed is False


def test_cow():
    cow = Cow()  # create instance to test

    assert isinstance(cow, Cow)
    assert cow.feed == "wheat"  # assert that feed is wheat
    assert cow.isfed is False  # asser that is not fed


def test_tiger():
    tiger = Tiger()

    assert isinstance(tiger, Tiger)
    assert tiger.feed == "meat"
    assert tiger.isfed is False


def test_elephant():
    elephant = Elephant()

    assert isinstance(elephant, Elephant)
    assert elephant.feed == "fruit"
    assert elephant.isfed is False

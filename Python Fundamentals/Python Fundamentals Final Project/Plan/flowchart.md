```mermaid
graph TD
    START([START]) --> MAIN_MENU

    MAIN_MENU["MENU - Main<br/>1. Show food schedule<br/>2. Show food storage<br/>3. Visit animals"]

    MAIN_MENU -->|1| FOOD_SCHEDULE_MENU
    MAIN_MENU -->|2| FOOD_STORAGE_MENU
    MAIN_MENU -->|3| VISIT_ANIMALS_MENU

    FOOD_SCHEDULE_MENU["MENU - Food Schedule<br/>Cow - Wheat<br/>Tiger - Meat<br/>Elephant - Fruit<br/>close"]
    FOOD_SCHEDULE_MENU -->|close| MAIN_MENU

    FOOD_STORAGE_MENU["MENU - Food Storage<br/>1. Wheat<br/>2. Meat<br/>3. Fruit<br/>close"]
    FOOD_STORAGE_MENU -->|close| MAIN_MENU
    FOOD_STORAGE_MENU -->|1| WHEAT[Wheat]
    FOOD_STORAGE_MENU -->|2| MEAT[Meat]
    FOOD_STORAGE_MENU -->|3| FRUIT[Fruit]

    WHEAT --> CHECK_HANDS
    MEAT --> CHECK_HANDS
    FRUIT --> CHECK_HANDS

    CHECK_HANDS{Already carrying food?}
    CHECK_HANDS -->|Yes| HANDS_FULL[Keep current food<br/>Show carrying limit]
    HANDS_FULL --> FOOD_STORAGE_MENU
    CHECK_HANDS -->|No| PICK_FOOD[Pick up one item<br/>Remember carried food]
    PICK_FOOD --> MAIN_MENU

    VISIT_ANIMALS_MENU["MENU - Visit Animals<br/>1. Cow<br/>2. Tiger<br/>3. Elephant<br/>close"]
    VISIT_ANIMALS_MENU -->|close| MAIN_MENU
    VISIT_ANIMALS_MENU -->|1| COW[Cow]
    VISIT_ANIMALS_MENU -->|2| TIGER[Tiger]
    VISIT_ANIMALS_MENU -->|3| ELEPHANT[Elephant]

    COW --> CHECK_FOOD
    TIGER --> CHECK_FOOD
    ELEPHANT --> CHECK_FOOD

    CHECK_FOOD{Carrying the correct food?}
    CHECK_FOOD -->|Yes| GIVE_FOOD[Give food<br/>Mark animal as fed<br/>Empty hands]
    CHECK_FOOD -->|No| CANNOT_FEED[Explain why feeding failed<br/>Keep carried food]

    GIVE_FOOD --> MAIN_MENU
    CANNOT_FEED --> MAIN_MENU


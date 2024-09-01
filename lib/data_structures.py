spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # names = []
    # for food in spicy_foods:
    #     names.append(food["name"])
    # return names

    # list comprehension
   return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # spiciest_foods = []
    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         spiciest_foods.append(food)
    # return spiciest_foods

    return [food for food in spicy_foods if food["heat_level"] > 5]
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        heat_level_str = "🌶" * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine: 
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    number_of_food = len(spicy_foods)

    average = total_heat // number_of_food
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

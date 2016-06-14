#python3

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def ask_for_preferences():
    preferences = {}
    for question in questions:
        answer = input(questions[question] + " (y/n): ")
        if answer.lower().strip() == "y": 
            preferences[question] = True
        else:
            preferences[question] = False
    return preferences

def make_drink(preferences):
    drink = []
    for type, liked in preferences.items():
        if liked:
            ingredient = random.choice(ingredients[type])
            drink.append(ingredient)
    return drink


def print_recipe(drink):
    pass
    # return desc

def name_drink(drink):
    adjectives = ingredients.keys()
    adjective = random.choice(adjectives) 
    pass
    # return string with name

def tell_drink(drink):
    print_recipe(drink)
    name_drink(drink)
  

# TO DO function to print recipes &
# TO DO give drink a name
# Extension exercises??

def carry_on():
    return False

if __name__ == "__main__":    
    another_one = True
    while another_one:
        preferences = ask_for_preferences()
        drink = make_drink(preferences)
        tell_drink(drink) 
        #function to print answer
        another_one = carry_on()
    

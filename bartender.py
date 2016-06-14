#python3

import random, sys

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
    if not len(drink):
        print("\nI cannot make drink with no ingredients.\nGet out!\n")
        sys.exit()
    return drink


def print_recipe(drink):
    print("\nJust for you a special drink with a:")
    for ingredient in drink:
        print(ingredient)
        

def name_drink():
    adjective = random.choice(list(ingredients.keys())) 
    noun = random.choice(["Sea-Dog", "Gorilla", "Chinchilla", "Baboon"])
    print("This drink I'll name '{} {}'\n".format(adjective.capitalize(), noun))

    
def tell_drink(drink):
    print_recipe(drink)
    name_drink()
  

def carry_on():
    answer = input("You like it? Can I make you another drink? (y/n): ")
    if answer.lower().strip() != "y":
        return False

# TODO: Extension exercises

if __name__ == "__main__": 
    print("\nWelcome to my bar! I'll make you a drink!\n")
    another_one = True
    while another_one:
        preferences = ask_for_preferences()
        drink = make_drink(preferences)
        tell_drink(drink) 
        another_one = carry_on()
    

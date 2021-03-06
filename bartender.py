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

def introduction():
    print("\nWelcome to my bar! I'll make you a drink!\n")
    name = input("So what's your name again? ")
    print("Hello {}, good to see you".format(name))
    return name

def ask_for_preferences():
    preferences = {}
    for question in questions:
        answer = input(questions[question] + " (y/n): ")
        if answer.lower().strip() in ["y", "yes"]: 
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
    if answer.lower().strip() not in ["y", "yes"]:
        print("No? Okay, see you around :-)\n")
        return False
    else:
        return True
        
def serve_other():
        others = input("Anyone else want a drink? (y/n): ")
        if others.lower().strip() not in ["y", "yes"]:
            return False
        else:
            return True

def main():
    serving = True
    while serving:
        #TODO customers should be a dict, storing key name + value drink
        customers = []
        name = introduction()
        customers.append(name)
        another_one = True
        #TODO should take into account if customer wants same drink 
        while another_one:
            preferences = ask_for_preferences()
            drink = make_drink(preferences)
            tell_drink(drink) 
            another_one = carry_on()
        serving = serve_other()
    

if __name__ == "__main__": 
    main()

    

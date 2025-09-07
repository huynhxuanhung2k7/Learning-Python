MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${RESOURCES['cost']}")


def ask():
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "off": 
        quit()
    elif ask == "report":
        report()
# TODO1: Print report of all coffee machine

# TODO2: Check resources sufficient?

# TODO3: Process coins

#TODO4: Check transaction successful?

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
print((MENU["espresso"]["ingredients"]))

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculate_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10          
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies 
    return total

def check_resources(coffee_type):
    total = calculate_money()
    for item in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][item] > RESOURCES[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    if total < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        for item in MENU[coffee_type]["ingredients"]:
            RESOURCES[item] -= MENU[coffee_type]["ingredients"][item]
        change = total - MENU[coffee_type]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
    return True

def report():
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")


def ask():
    continue_coffee = True
    while continue_coffee:
        ask = input("What would you like? (espresso/latte/cappuccino): ")
        if ask == "off": 
            quit()
        elif ask == "report":
            report()
        elif ask in MENU:
            check_resources(ask)
            continue_coffee = False
            
def main():
    while True:
        ask()
if __name__ == "__main__":
    main()


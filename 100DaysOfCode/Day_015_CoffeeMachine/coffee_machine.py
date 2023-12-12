from replit import clear

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_VALUES = {
    "pennies": 0.01,
    "nickels": 0.05, 
    "dimes": 0.10,
    "quarters": 0.25,
}

DRINKS = list(MENU.keys())


def report():
    for item, quantity in resources.items():
        print(f"{item}: {quantity}")


def is_resource_sufficient(drink):
    for ingredient, required_amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    return sum(COIN_VALUES[coin] * int(input(f"How many {coin}? ")) for coin in COIN_VALUES)


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print(f"Not enough money. Here's your money back: ${money_received:.2f}")
        return False


def make_coffee(drink):
    for item, quantity in MENU[drink]["ingredients"].items():
        resources[item] -= quantity
    print(f"Here is your {drink}! :)")


def coffee_machine():
    clear()
    while True: 
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "report":
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(choice):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice)
                    break
        else:
            print("Invalid choice. Please select a valid drink.")


def main():
    while True:
        coffee_machine()
        if input("Would you like another coffee? (y/n): ").lower() != 'y':
            break

main()
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    options = menu.get_items()
    choice = str(input(f"Make a selection ({options}): ")).strip().lower()
    if choice == "off":
        print("Power Off.")
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        print(f"Price of {drink.name} = ${drink.cost}")
        if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)

    
    
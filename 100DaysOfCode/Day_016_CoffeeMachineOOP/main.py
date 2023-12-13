from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

drinks_available = menu.get_items()


def coffee():
    machine_on = True
    while machine_on:
        try:
            drink_name = str(input(f"What would you like? ({drinks_available}): ")).strip().lower()
            if (menu.find_drink(drink_name)) or ("off") or ("report"):
                raise ValueError("Invalid input. Please only enter available drinks!")
            break
        except ValueError as e:
                    print(e)

        if machine_on == "off":
            machine_on = False
        elif drink_name == "report":
            CoffeeMaker().report()

coffee()
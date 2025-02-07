from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

coffee_maker= CoffeeMaker()
menu = Menu()
money=MoneyMachine()
drink_items=['latte', 'espresso', 'cappuccino']

clear_screen=lambda: os.system('cls' if os.name=='nt' else 'clear')

coffee_available=True
while coffee_available:
    
    prompt=str(input(f"Make a selection {menu.get_items()}: ")).strip().lower()
    drink=menu.find_drink(prompt)
    name=drink.name
    cost=drink.cost
    ingredients=drink.ingredients
    if not coffee_maker.is_resource_sufficient(drink):
        print(f"Not enough resources: {coffee_maker.report()}. Refill and turn machine back on!")
        break
    print(f"Your {name} is going to cost: {cost}")
    payment=money.make_payment(cost)
    if payment:
        clear_screen()
        coffee_maker.make_coffee(drink)
        print('\n')
    else:
        continue


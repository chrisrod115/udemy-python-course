import os
import random
import art
from game_data import data

LOGO=art.logo
VS=art.vs
SCORE=0

clear_screen=lambda:os.system('cls' if os.name=='nt' else 'clear')


def get_random_data(data):
    return random.choice(data)


def compare_options(choice, option_one, option_two):
    if choice == 'a':
        return option_two < option_one
    elif choice == 'b':
        return option_one < option_two


playing=True
while playing:
    clear_screen()
    print(f"Current Score = {SCORE}")
    option_one=get_random_data(data)
    option_two=get_random_data(data)
    if option_one==option_two:
        option_two=get_random_data(data)
    while True:
        try:
            print(f"Compare A: {option_one['name']} a {option_one['description']}, from {option_one['country']}.")
            print(VS)
            print(f"Against B: {option_two['name']} a {option_two['description']}, from {option_two['country']}.\n")
            choice=str(input(f"Who has a higher follower count, a or b: ")).lower().strip()
            if choice not in ['a','b']:
                print("Only enter the letters a or b!")
            else:
                break
        except ValueError:
            print("Invalid input type. Only enter letters.")
    res=compare_options(choice, option_one['follower_count'], option_two['follower_count'])
    if res:
        SCORE+=1
        continue
    clear_screen()
    print("Game Over!")
    print(f"Final Score = {SCORE}")
    break
    
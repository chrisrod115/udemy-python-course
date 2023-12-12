from art import logo, vs
from game_data import data
from replit import clear
import random

def starting_sequence():
    clear()
    print(logo)

def get_unique_choices(data):
    first = random.choice(data)
    second = random.choice(data)
    while first == second:
        second = random.choice(data)
    return first, second

def higher_or_lower(a, b, guess):
    if guess == 'a' and a['follower_count'] > b['follower_count']:
        return True
    if guess == 'b' and a['follower_count'] < b['follower_count']:
        return True
    return False

def higher_lower():
    score = 0
    while True:
        starting_sequence()
        first, second = get_unique_choices(data)
        print(f"Compare A: {first['name']}, a {first['description']} from {first['country']}")
        print(vs)
        print(f"Compare B: {second['name']}, a {second['description']} from {second['country']}")
        guess = input("Who has more followers? Type 'a' or 'b': ").lower().strip()

        if higher_or_lower(first, second, guess):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

def play_game():
    while True:
        higher_lower()
        if input("Play again? Type 'y' for yes or 'n' for no: ").lower() != 'y':
            break

play_game()

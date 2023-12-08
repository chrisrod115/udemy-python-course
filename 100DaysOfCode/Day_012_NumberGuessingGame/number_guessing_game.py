import random
from replit import clear

DIFFICULTY_TYPE = {'easy': 10, 'hard': 5}


def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if difficulty in DIFFICULTY_TYPE:
            return DIFFICULTY_TYPE[difficulty]
        print("Invalid input. Please type 'easy' or 'hard'.")


def check_guess(guess, hidden):
    if guess == hidden:
        return "win"
    return "higher" if guess < hidden else "lower"


def play_game():
    clear()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = get_difficulty()

    while attempts > 0:
        print(f"Lives left: {attempts}")
        guess = int(input("Make a guess: "))

        result = check_guess(guess, secret_number)
        if result == "win":
            print("Congrats! You guessed the number correctly!")
            return
        else:
            print(f"Wrong guess! Try going {result}.")
        
        attempts -= 1

    print(f"You've run out of lives. The number was {secret_number}.")


while True:
    play_game()
    
    while True:
        try:
            play_again = input("Would you like to play again (y/n): ").lower().strip()
            if play_again not in ['y', 'n']:
                raise ValueError("Invalid input. Please enter 'y' for yes or 'n' for no.")
            break
        except ValueError as e:
            print(e)

    if play_again == 'n':
        break
    
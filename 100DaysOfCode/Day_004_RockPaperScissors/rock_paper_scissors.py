import random
import os

ROCK = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
        (____)
---.__(___)
'''

CHOICES = {
    1: ROCK,
    2: PAPER,
    3: SCISSORS,
}

def determine_winner(bot_choice, player_choice):
    if bot_choice == player_choice:
        return "tie"
    elif (bot_choice == 1 and player_choice == 3) or \
         (bot_choice == 2 and player_choice == 1) or \
         (bot_choice == 3 and player_choice == 2):
        return "lose"
    else:
        return "win"

def play_game():
    clear_screen()
    bot_choice = random.randint(1, 3)
    while True:  # Input validation loop
        try:
            player_choice = int(input("Enter 1 (rock), 2 (paper), or 3 (scissors): "))
            if 1 <= player_choice <= 3:
                break  # Valid input, exit the loop
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Bot chose:\n{CHOICES[bot_choice]}")  # Use dictionary for lookup and cleaner printing
    print(f"You chose:\n{CHOICES[player_choice]}")

    result = determine_winner(bot_choice, player_choice)
    if result == "win":
        print("You win!")
    elif result == "tie":
        print("It's a tie!")
    else:
        print("You lose!")

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Cross-platform clear

while True:
    play_game()
    play_again = input("Would you like to play again? (y/n): ").strip().lower()
    if play_again != "y":
        break
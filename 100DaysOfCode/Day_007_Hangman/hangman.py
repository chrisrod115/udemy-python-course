# Hangman Game
# This is my personal version of the classic Hangman game.
# Created as part of my learning journey in Python programming.
# I did not have enough time to add in the art and name file.

import random

hangman_words = ["lory", "chris", "tovis"]

def user_letter():
    user_letter_input = str(input("Guess a letter: ")).strip().lower()
    if not user_letter_input:
        print("Please enter a letter.")
        return False
    return user_letter_input

def correct_letter(letter, word):
    return letter in word

def check_for_underscore(under):
    return "_" in under

def update_underscores(u_letter, hidden_word, underscores):
    for i in range(len(hidden_word)):
        if hidden_word[i] == u_letter:
            underscores[i] = u_letter

playing_hangman = True
while playing_hangman:
    hidden_word = random.choice(hangman_words)
    underscores = ["_" for _ in hidden_word]
    lives = 10

    while lives > 0 and check_for_underscore(underscores):
        print(' '.join(underscores))
        letter = user_letter()
        if letter == False:
            continue
        if correct_letter(letter, hidden_word):
            update_underscores(letter, hidden_word, underscores)
            if not check_for_underscore(underscores):
                print(' '.join(underscores))
                print("Winner!")
                break
            else:
                print("Correct Guess!")
        else:
            lives -= 1
            print(f"Incorrect. You have {lives} lives left.")

    if lives == 0:
        print("Sorry, you lost! The word was:", hidden_word)

    playing_hangman = False

import random

hangman_words = ["lory", "chris", "tovis"]
lives = 10


def display_to_console(word):
    underscore_list = ["_" for _ in word]
    print(f"Missing Letters: " + " ".join(underscore_list))


def update_word_display(letter_guess, word, underscore_list):
    for i, char in enumerate(word):
        if char == letter_guess:
            underscore_list[i] = letter_guess
    return underscore_list


def play_hangman(lives, word, underscore_list):
    guessed_letters = set()  # Initialize guessed_letters as a set
    while lives > 0 and "_" in underscore_list:
        print(f"Lives left: {lives}")
        print(f"Secret Word: {" ".join(underscore_list)}")
        u_input = input("Guess a letter: ").strip().lower()

        if u_input in guessed_letters:
            print(f"Guess again, already made guess: {u_input}")
        elif u_input in word:
            underscore_list = update_word_display(u_input, word, underscore_list)
        else:
            lives -= 1

        guessed_letters.add(u_input)  # Add guessed letter to the set

    if "_" not in underscore_list:
        print("Winner\n")
    else:
        print("Sorry you lost!\n")


rand_word = random.choice(hangman_words)
underscore_list = ["_" for _ in rand_word]  # Initialize underscore_list with underscores


def main():
    play_hangman(lives, rand_word, underscore_list)


if __name__ == '__main__':
    main()

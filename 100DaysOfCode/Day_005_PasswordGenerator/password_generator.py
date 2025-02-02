import random as r
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+"

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def get_positive_integer_input(prompt):
    while True:
        try:
            clear_screen()
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid Input. Only enter an integer.")

def password_generator(letters_count, numbers_count, symbols_count):
    password_characters = []  
    
    for _ in range(letters_count):
        password_characters.append(r.choice(alphabet))
    for _ in range(numbers_count):
        password_characters.append(r.choice(numbers))
    for _ in range(symbols_count):
        password_characters.append(r.choice(symbols))

    r.shuffle(password_characters)  
    return "".join(password_characters)  


print("Welcome to the PyPassword Generator!")
number_of_letters = get_positive_integer_input("How many letters would you like in your password?\n")
number_of_symbols = get_positive_integer_input("How many symbols would you like?\n")
number_of_numbers = get_positive_integer_input("How many numbers would you like?\n")

clear_screen()
password = password_generator(number_of_letters, number_of_symbols, number_of_numbers)
print(f"Your generated password is: {password}") 
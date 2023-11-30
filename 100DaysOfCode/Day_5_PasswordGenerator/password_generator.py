import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+"
numbers = "1234567890"
print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for i in range(0, number_of_letters):
    password += random.choice(alphabet)
for i in range(0, number_of_symbols):
    password += random.choice(symbols)
for i in range(0, number_of_numbers):
    password += random.choice(numbers)
password = ''.join(random.sample(password, len(password)))
print(f"Your password is: {password}")

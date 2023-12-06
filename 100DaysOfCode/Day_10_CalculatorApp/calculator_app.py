def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    if second == 0:
        return "Cannot divide by zero"
    return first / second

calculator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Welcome to the Calculator App.")

try:
    user_first = float(input("Enter the first number: ").strip())
    operation = input("Enter an operation (+, -, *, /): ").strip()
    user_second = float(input("Enter your second number: ").strip())

    if operation in calculator_dictionary:
        result = calculator_dictionary[operation](user_first, user_second)
        print("Result:", result)
    else:
        print("Invalid operation.")
except ValueError:
    print("Invalid input. Please enter a number.")

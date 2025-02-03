import os

OPERATORS=['+','-','*','/']


clear_screen=lambda:os.system('cls' if os.name=='nt' else 'clear')


# calculator app
def do_the_maths(num1, num2, operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    else:
        return num1/num2


calculating=True
while calculating:
    clear_screen()
    print("Calculator App!")
    # Input number 1:
    number_one=int(input("Enter the first number: "))
    # Input number 2:
    number_two=int(input("Enter the second number: "))
    # Input an operator:
    while True:
        operator=str(input("Enter the operator either (+, -, /, *): "))
        if operator in OPERATORS:
            print(do_the_maths(number_one, number_two, operator))
            break
        print("Invalid Input. Only enter the following symbols: (+, -, /, *).\n")
    again=str(input("Would you like to calculate something else? (Y/N) ")).strip().lower()
    if (again=='y'):
        continue
    else:
        break
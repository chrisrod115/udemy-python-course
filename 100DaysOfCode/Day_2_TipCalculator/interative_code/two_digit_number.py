"""METHOD 1: Using a for loop.
"""

# two_digit_number = input("Type a two digit number: ")
# total_result = 0
# for digit in two_digit_number:
#     total_result += int(digit)
# print(total_result)


"""METHOD 2: Using indexing.
"""
two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
total_result = int(first_digit) + int(second_digit)
print(total_result)
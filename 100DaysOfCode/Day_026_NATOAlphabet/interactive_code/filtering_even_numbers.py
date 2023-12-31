list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_ints = [int(i) for i in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [x for x in list_of_ints if x % 2 == 0]


# Write your code 👆 above:

print(result)

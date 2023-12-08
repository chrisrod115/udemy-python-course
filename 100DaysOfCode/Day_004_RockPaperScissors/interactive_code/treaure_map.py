"""METHOD 1: My attempt --> too complicated can be simplified with (method 2) below.
"""
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# position.upper()
# # print(map) # Used this to see how the list was formatted. 
# column = ["A", "B", "C"]
# row = [0, 1, 2]
# p_col = position[0]
# p_row = int(position[1]) - 1
# for y in range(3):
#     if p_row == row[y]:
#         for x in range(3):
#             if p_col == column[x]:
#                 map[y][x] = "X"
    

# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

"""METHOD 2: Second method provided by instructor, which is using the index attribute. 
"""
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
    

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
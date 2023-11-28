"""METHOD 1: My personal method.
"""
# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random 
# print(random.choice(names) + " is going to buy the meal today!")

"""METHOD 2: Other methods.
"""
import random 

names_string = "ben, tom, bob"
names = names_string.split(", ") 
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
random_name = names[random_choice]
print(f"{random_name} is going to buy the meal today!")

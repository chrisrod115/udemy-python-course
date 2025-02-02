print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

treasure_map={
    "choice_one": {
        "prompt": "You're at a cross road. Where do you want to go? Type 'left' or 'right'. ",
        "left": True,
        "right": False,
    },
    "choice_two": {
        "prompt": "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ",
        "wait": True,
        "swim": False,
    },
    "choice_three": {
        "prompt": "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ",
        "red": {
                "prompt": "It's a room full of fire. Game Over.",
                },
        "yellow": {
                   "prompt": "You found the treasure! You Win!",
                   },
        "blue": {
                 "prompt": "You fell of the earth, you die! Game over!",
                 },
    },
    "lost": "You get attacked by an angry trout. Game Over.",
}



left_right=input(str(treasure_map["choice_one"]["prompt"])).strip().lower()
if (treasure_map["choice_one"][left_right]):
    wait_swim=input(str(treasure_map["choice_two"]["prompt"])).strip().lower()
    if (treasure_map["choice_two"][wait_swim]):
        red_yellow_blue=input(str(treasure_map["choice_three"]["prompt"])).strip().lower()
        if (treasure_map["choice_three"][red_yellow_blue]):
            print(treasure_map["choice_three"][red_yellow_blue]["prompt"])
    else:
        print(treasure_map["lost"])
else:
    print(treasure_map["lost"])
        


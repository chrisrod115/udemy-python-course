rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rpc = [rock, paper, scissors]
player_choice = str(input(f"Choose either: rock, paper, or scissors ")).lower()
rpc_index = ["rock", "paper", "scissors"]
player_choice = rpc[rpc_index.index(player_choice)]
bot_choice = random.choice(rpc)

print(f"You chose: {player_choice}")
print(f"\nBot chose: {bot_choice}")
if player_choice == bot_choice:
    print("Tie")
elif (player_choice == rock) and (bot_choice == scissors):
    print("Winner")
elif (player_choice == scissors) and (bot_choice == paper):
    print("Winner")
else:
    print("Lost")
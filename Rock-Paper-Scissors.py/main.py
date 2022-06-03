# This is a Rock-Paper-Scissors Task
#importing a random

import random

my_action = input("rock, paper or scissors?:")
opponent_action = random.choice(["rock", "paper", "scissors"])

print(f"My choice is: {my_action}")
print(f"Opponent Choose: {opponent_action}")

if my_action == opponent_action:
    print(f"It's a tie. Both of you selected {my_action}")

elif my_action == "rock":
    if opponent_action =="scissors":
        print("Rock smashes scissors.. I win!!")
    else:
        print("Opponent Win!! paper covers rock")
elif my_action == "paper":
    if opponent_action == "rock":
        print("I win!!! paper covers rock")
    else:
        print("Opponent Win!! scissors cut paper")
elif my_action == "scissors":
    if opponent_action == "paper":
        print("I Win!!! Scissors cut paper")
    else:
        print("Opponent Win.. Rock smashes scissors")

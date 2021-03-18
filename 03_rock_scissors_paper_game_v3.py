# randint - generate random int

import random

print("Let's play a game! \n***rock, scissors, paper***")

player = input("Hey human, make your move: ").lower()

rand_num = random.randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
    
print(f"Computer plays: {computer}")

if player == computer:
    print("It's a tie")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "scissors":
        print("computer wins!")
    elif computer == "rock":
        print("player wins!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
        print("computer wins!")
else:
    print("something went wrong!")

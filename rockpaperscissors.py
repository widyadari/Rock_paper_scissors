#import modules
import random 

#options for the game
player = ["Rock", "Paper", "Scissors"]
computer = random.choice(player)

#start the game
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Type in your choice:")

if computer == user_choice:
    print("It's a draw")
elif computer == "Paper" and user_choice == "Scissors":
    print("You win!")
elif computer == "Rock" and user_choice == "Paper":
    print("You win!")
elif computer == "Scissors" and user_choice == "Rock":
    print("You win!")
elif computer == "Scissors" and user_choice == "Paper":
    print("You lose!")
elif computer == "Rock" and user_choice == "Scissors":
    print("You lose!")
elif computer == "Paper" and user_choice == "Rock":
    print("You lose!")
else :
    print ("WRONG INPUT")
# Solution for the week 02 lab
import random
choices = ["Rock", "Paper", "Scissors"]
print(choices)

playerChoice = input("Enter a number between 1 - 3 for the following choices -> 1 = Rock, 2 = Paper, 3 = Scissors : ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error! Choice should be between 1 and 3.")
else: 
    # Develop the game logic using if/else/elif statements
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("You win! Rock beats Scissors.")
    elif playerChoice == 2 and computerChoice == 1:
        print("You win! Paper beats Rock.")
    elif playerChoice == 3 and computerChoice == 2:
        print("You win! Scissors beats Paper.")
    else:
        print("You lose!")
    
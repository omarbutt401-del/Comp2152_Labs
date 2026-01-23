# Solution for the week 02 lab
choices = ["Rock", "Paper", "Scissors"]

player = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(player)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    computer = input("Enter computer's choice (1-3): ")
    computer = int(computer)
    
    if computer < 1 or computer > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        playerName = choices[playerChoice -1]
        computerName = choices[computer -1]
        
        print(f"You chose: {playerName}")
        print(f"Computer chose: {computerName}")

        if playerChoice == computer:
            print("It's a tie!")
        elif player == 1 and computer == 3:
            print("Rock beats Scissors - You win!")
        elif player == 2 and computer == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computer == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")
        
        if playerName != "Rock":
            print("You didn't pick the classic Rock...")
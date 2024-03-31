import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors? ").lower().strip()

    print("Computer choice: " + computer)
    print("Player choice: " + player)

    if player == computer:
        print("Tie!")
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors") or (player == "scissors" and computer == "rock"):
        print("You lost!")
    else:
        print("You won!")
        
    play_again = input("Play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        break
    print("")
    
print("Bye!")


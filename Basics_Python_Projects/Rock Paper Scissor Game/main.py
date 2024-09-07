import random
options = ("rock", "paper", "scissor")

running  = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:   
        player = input("Enter a choice (rock , paper , scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissor":
        print("You Win! ")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissor" and computer == "paper":
        print("You Win")      
    else:
        print("You Lose!") 

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
    print("Thanks For Playing")           
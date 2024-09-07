import random

lowest_num = 1
highest_num  = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = 0

print("Python Number  Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")


while  is_running:
    guess  = input("Enter Your Guess")

    if guess.isdigit():
        guess = int(guess)
        guesses =+ 1

        if guess < lowest_num or guess > highest_num:
            print("That Number is Out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Two Low! Try Again!")
        elif guess > answer:
            print("Too high! Try Again")  
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")  
            is_running = False      
        
       
    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")


    
    

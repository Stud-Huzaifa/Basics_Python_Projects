questions = [
    "Which planet is known as the Red Planet?",
    "Which animal is known as the King of the Jungle?",
    "How many continents are there in the world?",
    "What is the capital of France?",
    "Which ocean is the largest in the world?"
]

options = [
    ("a) Earth", "b) Jupiter", "c) Mars", "d) Venus"),
    ("a) Elephant", "b) Lion", "c) Tiger", "d) Giraffe"),
    ("a) 5", "b) 6", "c) 7", "d) 8"),
    ("a) Berlin", "b) Paris", "c) Rome", "d) Madrid"),
    ("a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean")
]

answers = ("C", "B", "C", "B", "C")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print(f"WRONG! The correct answer is {answers[questions_num]}")
    
    questions_num += 1

print("-----------------")
print("     RESULTS   ")   
print("------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"Your Score is: {score_percentage}%")

#END OF THE PROGRAM

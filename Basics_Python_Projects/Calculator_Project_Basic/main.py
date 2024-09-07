operator = input("Enter an operator (+ - / *): ")
num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))

if operator == '+':
    result = num1 + num2
    print(round(result, 3))

elif operator == '-':
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == '/':
    if num2 == 0:
        print("Invalid Operation: Division by Zero")
    else:
        result = num1 / num2
        print(round(result, 3))

else:
    print(f"{operator} is not a valid operator")

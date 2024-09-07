#TEMPERATURE CONVERSION


unit = input("Is This Temperature in Celsius or Fahrenheit (C/F): ")
temp =float(input("Enter Your Temperature: "))

if unit == "F":
    temp = round((9*temp) / 5 + 32, 1) 
    print(f"The Temperature in Fahrenheit  is : {temp}")
elif unit == "C":
    temp = (round(temp - 32 ) *5/9, 1)
else:
    print(f"{unit} is an invalid  unit of measurement! ")
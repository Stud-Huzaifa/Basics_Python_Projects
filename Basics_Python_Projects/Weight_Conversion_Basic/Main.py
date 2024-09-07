#WEIGHT CONVERSION

weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (K or P): ")

if unit.upper() == "K":  # Accept both lowercase 'k' and uppercase 'K'
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your Weight is: {round(weight, 1)} {unit}")
    
elif unit.upper() == "P":  # Accept both lowercase 'p' and uppercase 'P'
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your Weight is: {round(weight, 1)} {unit}")
    
else:
    print(f"'{unit}' is not a valid option.")

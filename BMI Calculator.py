#Kevin
#BMI calculator

sum = 0

while True:

    # 1.Input
    x1 = float(input("Enter your weight in kilograms       : ")) 
    x2 = float(input("Enter your height in meters          : "))

    # 2.Process
    sum = x1/x2**2

    # 3. Output
    print(f"Your BMI is: {sum}")
    res = input("Continue? (Yes/No): ")
    if res == "No":
        break;
#Kevin

#Calculator adding 2 value

sum = 0

while True:
    # 1.Input
    x1 = input("Type x1= ") 
    x2 = input("Type x2= ")
    op = input('Enter operator (+,-,*,/): ')

    # 2.Process
    if op == '+':
    sum = int(x1)+int(x2)
    elif op == '-':
    sum = int(x1)-int(x2)

    # 3. Output
    print(f"Sum: {sum}")
    res = input("Continue? (Y/N)")
    if res == "N":
        break;
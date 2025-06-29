
expression = input("Expression: ")
x, y, z = expression.split()

add = int(x) + int(z)
subtract = int(x) - int(z)
multiplication = int(x) * int(z)
division = int(x) / int(z)

if y == '+':
    print(f"{add:.1f}")
elif y == '*':
    print(f"{multiplication:.1f}")
elif y == '/':
    print(f"{division:.1f}")
elif y == '-':
    print(f"{subtract:.1f}")
else:
    print("Invalid Input")
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

op = input("Enter operation(+,-,*,/,%): ")

if op == '+':
    print("Result:", num1 + num2)

elif op == '-':
    print("Result:", num1 - num2)

elif op == '*':
    print("Result:", num1* num2)

elif op == '/':
    print("Result:", num1 / num2)
elif op == '%':
    print("Result:", num1 % num2)
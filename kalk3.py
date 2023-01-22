import math

def calculator():
    while True:
        operation = input("Enter q for quit, enter operation (+, -, *, /, %, **, log, sin, cos, tan, cot, csc, sec, sqrt): ")
        if operation == 'q':
            break
        elif operation in ['+', '-', '*', '/', '%', '**']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if operation == '+':
                print("Result: ", x+y)
            elif operation == '-':
                print("Result: ", x-y)
            elif operation == '*':
                print("Result: ", x*y)
            elif operation == '/':
                print("Result: ", x/y)
            elif operation == '%':
                print("Result: ", x%y)
            elif operation == '**':
                print("Result: ", x**y)
        elif operation in ['log', 'sin', 'cos', 'tan', 'cot', 'csc', 'sec', 'sqrt']:
            x = float(input("Enter number: "))

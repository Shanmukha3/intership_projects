def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please choose a valid operation.")
        calculator()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print(f"Result: {result}")

while(1):
    print()
    print('1.To perform calculation')
    print('2.TO exit')
    n=int(input('enter the required choice'))
    if n==1:
        calculator()
    elif n == 2:
        print('Thank you :)')
        break  
    else:
        print('Invalid choice. Please enter 1 or 2.')


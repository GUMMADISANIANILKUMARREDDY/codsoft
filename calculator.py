import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def exponentiation(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x // y

def square_root(x):
    if x < 0:
        return "Cannot find square root of a negative number"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm"
    return math.log(x, base)

# Operations dictionary
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Exponentiation", exponentiation),
    "6": ("Modulus", modulus),
    "7": ("Floor Division", floor_division),
    "8": ("Square Root", square_root),
    "9": ("Natural Logarithm", math.log),
    "10": ("Base-10 Logarithm", lambda x: logarithm(x, 10)),
    "11": ("Base-2 Logarithm", lambda x: logarithm(x, 2)),
    "12": ("Base-e Logarithm", lambda x: logarithm(x, math.e)),
}

print("Operations:")
for key, value in operations.items():
    print(f"{key}: {value[0]}")

choice = input("Enter the operation number you want to perform: ")

if choice in operations:
    if choice in ["8", "9", "10", "11", "12"]:
        num = float(input("Enter the number: "))
        result = operations[choice][1](num)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[choice][1](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation choice")

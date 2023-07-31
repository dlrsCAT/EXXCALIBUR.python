def main():
    return 5 + 3


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = float(input("Enter the first number: "))


num2 = float(input("Enter the second number: "))







operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == "/":
    print(num1, "/", num2, "=", divide(num1, num2))



def main():
    return 5 + 3


# Define the function to perform addition
def add(x, y):
    return x + y


# Define the function to perform subtraction
def subtract(x, y):
    return x - y

# Define the function to perform multiplication
def multiply(x, y):
    return x * y

# Ask the user for the first number
num1 = float(input("Enter the first number: "))


# Ask the user for the second number
num2 = float(input("Enter the second number: "))



# Ask the user for the operation to perform
operation = input("Enter the operation (+, -, *, /): ")


# Perform the operation based on user input
if operation == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
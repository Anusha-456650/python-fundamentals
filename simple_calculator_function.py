# Function to perform basic arithmetic operations

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ").strip()

# Calling function
result = calculate(num1, num2, op)

# Printing result
print(f"Result: {result}")
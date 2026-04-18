# Function to check whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Taking input from user
number = int(input("Enter a number: "))

# Calling function
result = check_even_odd(number)

# Printing result
print(f"{number} is {result}")
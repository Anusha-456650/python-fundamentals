# Demonstrates conditional statements (if, else, elif) in python

# Taking input from user
age = int(input("Please enter your age: "))

# Applying conditional logic
if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen")



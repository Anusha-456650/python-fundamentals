# Print even and odd numbers upto user input

# Taking input from the user
n = int(input("Please enter a number: "))

for i in range(1,(n+1)):
    result = print(f'{i} is an even') if i % 2 == 0 else  print(f'{i} is an odd')


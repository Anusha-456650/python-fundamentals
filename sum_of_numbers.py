# Calculate sum from 1 to user input

# Taking input from the user
n = int(input("Please enter a number: "))
total =0

for i in range(1, n+1):
    total += i

print(f'\nsum from 1 to {n} is : {total}')
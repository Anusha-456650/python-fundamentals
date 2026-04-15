# Demonstrates user input, f-strings, and print formatting options in python

#Taking input from user
name = input("Please enter your name: ")
age = input("Please enter your age: ")
city = input("Please enter your city: ")

# Using f-string to format output in a clean way
print(f"\nUser Details: Name = {name}, Age = {age}, city = {city}")

# Using sep parameter to control spacing between multiple values
print("Python","is","fun", sep="-")

# USing end parameter to control end behavior of print
print("Learning Python",end = " ")
print("is interesting!")
# Keeps asking until correct password is entered

correct_password = "Python@123"

while True:
    user_input = input("Enter your password: ").strip()

    if user_input == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect password, try again.")
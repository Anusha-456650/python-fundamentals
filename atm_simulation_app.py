# ATM Simulation Application using functions

def withdraw_balance(balance, amount):
    if amount <= 0:
        return balance, "Invalid amount entered."
    elif amount > balance:
        return balance, "Insufficient balance."
    else:
        balance -= amount
        return balance, f"Withdrawal successful! Remaining balance: {balance}"


def main():
    print("=== ATM Simulation ===")

    # Initial balance
    balance = 1000

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"Your current balance is: {balance}")

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            balance, message = withdraw_balance(balance, amount)
            print(message)

        elif choice == "3":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()
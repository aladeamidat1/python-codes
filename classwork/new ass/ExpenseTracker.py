import datetime

# List to store expenses
expenses = []


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
        expenses.append({"date": date, "description": description, "amount": amount})
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\nExpenses:")
    print("Date", "Description", "Amount")
    print("-" * 45)
    for exp in expenses:
        print("{:<12} {:<20} ${:<10.2f}".format(exp["date"], exp["description"], exp["amount"]))
    print()


def calculate_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expenses: ${total:.2f}\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

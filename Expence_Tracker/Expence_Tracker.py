import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(expenses, category, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if category in expenses:
        expenses[category].append({"timestamp": timestamp, "amount": amount})
    else:
        expenses[category] = [{"timestamp": timestamp, "amount": amount}]

def view_expenses(expenses):
    for category, items in expenses.items():
        total_amount = sum(item["amount"] for item in items)
        print(f"{category}: Rs.{total_amount:.2f}")

def generate_report(expenses):
    print("\nExpense Report:")
    view_expenses(expenses)
    total_expenses = sum(sum(item["amount"] for item in items) for items in expenses.values())
    print(f"Total Expenses: ${total_expenses:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
            print("Expense added successfully!")
        elif choice == '2':
            if expenses:
                print("\nExpenses:")
                view_expenses(expenses)
            else:
                print("No expenses recorded yet.")
        elif choice == '3':
            if expenses:
                generate_report(expenses)
            else:
                print("No expenses recorded yet.")
        elif choice == '4':
            print("Saving expenses and exiting Expense Tracker.")
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

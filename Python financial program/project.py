import csv
from datetime import datetime

def main():
    print("Welcome to Personal Finance Manager!")
    while True:
        print("\nChoose an option:")
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. View summary by category")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please try again.")
        return

    category = input("Enter the category (e.g., Food, Rent, Utilities): ")
    description = input("Enter a description: ")
    amount = input("Enter the amount (positive for income, negative for expense): ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Transaction added successfully!")

def view_transactions():
    try:
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            print("\nDate       | Category   | Description         | Amount")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]:<10} | {row[1]:<10} | {row[2]:<20} | {float(row[3]):>7.2f}")
    except FileNotFoundError:
        print("No transactions found. Please add some first.")

def view_summary_by_category():
    try:
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            summary = {}
            for row in reader:
                category = row[1]
                amount = float(row[3])
                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

            print("\nCategory   | Total Amount")
            print("-" * 30)
            for category, total in summary.items():
                print(f"{category:<10} | {total:>12.2f}")
    except FileNotFoundError:
        print("No transactions found. Please add some first.")

if __name__ == "__main__":
    main()

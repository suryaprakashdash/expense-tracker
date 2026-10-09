#       PERSONAL EXPENSE TRACKER

# List to store all expenses
expenses = []


# ------------------------------------------
# 1. Add Expense
# ------------------------------------------
def add_expense():
    print("\nADD EXPENSE")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category (Food/Travel/Shopping/etc.): ").strip()

        if category == "":
            print("Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        if description == "":
            description = "No description"

        # Create a dictionary for the expense
        expense = {
            "amount": amount,
            "category": category.title(),
            "description": description
        }

        # Store the dictionary in the list
        expenses.append(expense)

        print("\nExpense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")


# ------------------------------------------
# 2. View All Expenses
# ------------------------------------------
def view_expenses():
    print("\n ALL EXPENSES")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("-" * 65)
    print(f"{'No.':<5}{'Category':<15}{'Amount':<15}{'Description'}")
    print("-" * 65)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['description']}"
        )

    print("-" * 65)


# ------------------------------------------
# 3. Calculate Total Expenses
# ------------------------------------------
def calculate_total():
    print("\nTOTAL EXPENSES")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total expenses: ₹{total:.2f}")


# ------------------------------------------
# 4. Search Expenses by Category
# ------------------------------------------
def search_by_category():
    print("\nSEARCH BY CATEGORY")

    if len(expenses) == 0:
        print("No expenses available to search.")
        return

    search_category = input("Enter category to search: ").strip().lower()

    if search_category == "":
        print("Category cannot be empty.")
        return

    found = False
    category_total = 0

    for index, expense in enumerate(expenses, start=1):
        if expense["category"].lower() == search_category:
            print(
                f"{index}. {expense['category']} - "
                f"₹{expense['amount']:.2f} - "
                f"{expense['description']}"
            )

            category_total += expense["amount"]
            found = True

    if found:
        print(f"Total for {search_category.title()}: ₹{category_total:.2f}")
    else:
        print("No expenses found in this category.")


# ------------------------------------------
# 5. Show Highest Expense
# ------------------------------------------
def show_highest_expense():
    print("\nHIGHEST EXPENSE")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print(f"Category: {highest['category']}")
    print(f"Amount: ₹{highest['amount']:.2f}")
    print(f"Description: {highest['description']}")


# ------------------------------------------
# 6. Delete an Expense
# ------------------------------------------
def delete_expense():
    print("\nDELETE EXPENSE")

    if len(expenses) == 0:
        print("No expenses available to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

        deleted_expense = expenses.pop(choice - 1)

        print("\nExpense deleted successfully!")
        print(
            f"Deleted: {deleted_expense['category']} - "
            f"₹{deleted_expense['amount']:.2f}"
        )

    except ValueError:
        print("Please enter a valid whole number.")


# ------------------------------------------
# 7. Main Menu
# ------------------------------------------
def main():
    while True:
        print("PERSONAL EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search by Category")
        print("5. Show Highest Expense")
        print("6. Delete an Expense")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                calculate_total()

            elif choice == 4:
                search_by_category()

            elif choice == 5:
                show_highest_expense()

            elif choice == 6:
                delete_expense()

            elif choice == 7:
                print("\nThank you for using Expense Tracker!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please select between 1 and 7.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# ------------------------------------------
# Program Execution
# ------------------------------------------
if __name__ == "__main__":
    main()


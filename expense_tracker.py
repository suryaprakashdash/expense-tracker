#PERSONAL EXPENSE TRACKER



# CLASS 1: Expense

class Expense:

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display_expense(self, index):
        print(
            f"{index:<5}"
            f"{self.category:<15}"
            f"Rs.{self.amount:<12.2f}"
            f"{self.description}"
        )

# CLASS 2: ExpenseTracker
class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    # 1. Add Expense
    def add_expense(self):
        print("\nADD EXPENSE")

        try:
            amount = float(input("Enter expense amount: Rs."))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            category = input("Enter category: ").strip()

            if not category:
                print("Category cannot be empty.")
                return

            description = input("Enter description: ").strip()

            if not description:
                description = "No description"

            expense = Expense(
                amount,
                category.title(),
                description
            )

            self.expenses.append(expense)

            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount! Enter a valid number.")

    # 2. View All Expenses
    def view_expenses(self):
        print("\nALL EXPENSES")

        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print("-" * 65)
        print(f"{'No.':<5}{'Category':<15}{'Amount':<15}{'Description'}")
        print("-" * 65)

        for index, expense in enumerate(self.expenses, start=1):
            expense.display_expense(index)

        print("-" * 65)

    # 3. Calculate Total Expenses
    def calculate_total(self):
        print("\nTOTAL EXPENSES")

        total = 0

        for expense in self.expenses:
            total += expense.amount

        print(f"Total expenses: Rs.{total:.2f}")

    # 4. Search by Category
    def search_by_category(self):
        print("\nSEARCH BY CATEGORY")

        if not self.expenses:
            print("No expenses available.")
            return

        search_category = input("Enter category to search: ").strip().lower()

        if not search_category:
            print("Category cannot be empty.")
            return

        found = False
        category_total = 0

        for index, expense in enumerate(self.expenses, start=1):
            if expense.category.lower() == search_category:
                expense.display_expense(index)
                category_total += expense.amount
                found = True

        if found:
            print(
                f"Total for {search_category.title()}: "
                f"Rs.{category_total:.2f}"
            )
        else:
            print("No expenses found in this category.")

    # 5. Show Highest Expense
    def show_highest_expense(self):
        print("\nHIGHEST EXPENSE")

        if not self.expenses:
            print("No expenses available.")
            return

        highest = self.expenses[0]

        for expense in self.expenses:
            if expense.amount > highest.amount:
                highest = expense

        print(f"Category: {highest.category}")
        print(f"Amount: Rs.{highest.amount:.2f}")
        print(f"Description: {highest.description}")

    # 6. Delete an Expense
    def delete_expense(self):
        print("\nDELETE EXPENSE")

        if not self.expenses:
            print("No expenses available to delete.")
            return

        self.view_expenses()

        try:
            choice = int(input("Enter expense number to delete: "))

            if choice < 1 or choice > len(self.expenses):
                print("Invalid expense number.")
                return

            deleted_expense = self.expenses.pop(choice - 1)

            print("Expense deleted successfully!")
            print(
                f"Deleted: {deleted_expense.category} - "
                f"Rs.{deleted_expense.amount:.2f}"
            )

        except ValueError:
            print("Please enter a valid whole number.")

    # 7. Main Menu
    def run(self):
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
                    self.add_expense()

                elif choice == 2:
                    self.view_expenses()

                elif choice == 3:
                    self.calculate_total()

                elif choice == 4:
                    self.search_by_category()

                elif choice == 5:
                    self.show_highest_expense()

                elif choice == 6:
                    self.delete_expense()

                elif choice == 7:
                    print("\nThank you for using Expense Tracker!")
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice! Select between 1 and 7.")

            except ValueError:
                print("Invalid input! Enter a whole number.")


# PROGRAM EXECUTION
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()


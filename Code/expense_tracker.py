# Personal Expense Tracker


# ============================================================
# Expense Data
# ============================================================

expense_records = [
    {
        "category": "Food",
        "amount": 200
    },
    {
        "category": "Travel",
        "amount": 150
    },
    {
        "category": "Food",
        "amount": 300
    },
    {
        "category": "Shopping",
        "amount": 270
    },
    {
        "category": "Travel",
        "amount": 410
    }
]


# ============================================================
# Add New Expense
# ============================================================

def add_expense():

    while True:
        try:
            new_amount = int(input("Enter the new expense amount: "))

            if new_amount >= 0:
                break
            else:
                print("Amount must be grater than 0.")
    
        except ValueError:
            print("Please enter a valid number.")
    

    new_category = input("Enter the category of new amount: ")

    new_expense = {
        "category": new_category,
        "amount": new_amount
    }

    expense_records.append(new_expense)

    print("Expense added successfully.")


# ============================================================
# View All Expenses
# ============================================================

def view_all_expenses():

    for record in expense_records:

        print(record["category"], record["amount"])


# ============================================================
# Show Expenses by Category
# ============================================================

def show_category_expenses(category):

    found = False

    for record in expense_records:

        if category.lower() == record["category"].lower():

            print(record["category"], record["amount"])

            found = True

    if not found:

        print("No expenses found for this category.")


# ============================================================
# Calculate Category Total
# ============================================================

def calculate_category_total(category):

    total = 0

    for record in expense_records:

        if category.lower() == record["category"].lower():

            total += record["amount"]

    return total


# ============================================================
# Expense Summary
# ============================================================

def expense_summary():

    amounts = []

    for record in expense_records:

        amounts.append(record["amount"])

    total_expense = sum(amounts)
    highest_expense = max(amounts)
    lowest_expense = min(amounts)
    average_expense = sum(amounts) / len(amounts)
    number_of_expenses = len(amounts)

    print("Total Expense:", total_expense)
    print("Highest Expense:", highest_expense)
    print("Lowest Expense:", lowest_expense)
    print("Average Expense:", average_expense)
    print("Number of Expenses:", number_of_expenses)


# ============================================================
# Check Budget
# ============================================================

def check_budget(budget):

    total = 0

    for record in expense_records:

        total += record["amount"]

    if total <= budget:

        print("Within budget.")

    else:

        print("Budget exceeded.")


# ============================================================
# Display Menu
# ============================================================

def show_menu():

    print("===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Category Expenses")
    print("4. Calculate Category Total")
    print("5. Expense Summary")
    print("6. Check Budget")
    print("7. Exit")


# ============================================================
# Main Menu Loop
# ============================================================

while True:

    show_menu()

    choice = input("Enter the option number (1-7): ")

    print("You selected:", choice)

    if choice == "1":

        add_expense()

    elif choice == "2":

        view_all_expenses()

    elif choice == "3":

        category = input("Enter category: ")

        show_category_expenses(category)

    elif choice == "4":

        category = input("Enter category: ")

        total = calculate_category_total(category)

        print("Total", category, "Expenses:", total)

    elif choice == "5":

        expense_summary()

    elif choice == "6":

        while True:

            try:       
                budget = int(input("Enter Budget Amount: "))

                if budget > 0:
                    break

                else:
                    print("Budget must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")


        check_budget(budget)

    elif choice == "7":

        print("Thank you for using Personal Expense Tracker.")

        break

    else:

        print("Invalid choice. Please enter a number from 1 to 7.")
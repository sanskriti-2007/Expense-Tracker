import csv

expenses = []
budget = 0

def set_budget(): 
    global budget
    budget = float(input("Enter budget: "))
    print("Budget set successfully.")

def budget_status():
    spent = calculate_total(expenses)
    remaining = budget - spent
    print(f"Budget - ₹{budget}")
    print(f"Money Spent - ₹{spent}")
    print(f"Money Remaining - ₹{remaining}")
    if remaining < 0:
        print("Budget exceeded!")

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    category = input("Category: ")
         
    expenses.append(
        {
            "name" : name,
            "amount" : amount, 
            "category" : category
        }
    )
    save_expenses(name, amount, category)
    print("Expense added.")


def view_expenses():
    for i, expense in enumerate(expenses, start = 1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']} ({expense['category']})")


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    category = "Uncategorized"
                elif len(row) == 3:
                    category = row[2]
                else:
                    continue
                expenses.append(
                    {
                    "name" : row[0],
                    "amount" : float(row[1]),
                    "category" : category
                    }
                )
    except FileNotFoundError:
        pass


def save_all_expenses():
    with open("expenses.csv", "w", newline = "") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([expense["name"], expense["amount"], expense["category"]])


def delete_expenses():
    view_expenses()

    number = int(input("Enter the number of expenses you want to delete: "))
    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        save_all_expenses()
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid number.")


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]
    
    return total


def show_total():
    print(f"Total Expenses: ₹{calculate_total(expenses)}")


def save_expenses(name, amount, category):
    with open("expenses.csv", "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])


def show_category_totals():
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category not in totals:
            totals[category] = amount
        else:
            totals[category] += amount

    for category, total in totals.items():
        print(f"{category} - ₹{total:.2f}")

def search_expense():
    search = input("Expense name: ").lower()
    for expense in expenses:
        if search == expense['name'].lower():
            print(f"{expense}")


def sort_expenses():
    print("1. Sort by Amount")
    print("2. Sort by Name")
    print("3. Sort by Category")
    option = int(input("Option: "))
    if option == 1:
       sorted_expense = sorted(expenses, key = lambda expense: expense['amount'])
       for expense in sorted_expense:
           print(f"{expense['name']} - ₹{expense['amount']} {(expense['category'])}")
    elif option == 2:
       sorted_expense = sorted(expenses, key = lambda expense: expense['name'])
       for expense in sorted_expense:
           print(f"{expense['name']} - ₹{expense['amount']} {(expense['category'])}")
    elif option == 3:
        sorted_expense = sorted(expenses, key = lambda expense: expense['category'])
        for expense in sorted_expense:
           print(f"{expense['name']} - ₹{expense['amount']} - {expense['category']}")
    else:
        print("Invalid option.")

load_expenses()

def main():
    while True:
        print("\nExpense Tracker.")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense(s)")
        print("4. Show Total")
        print("5. View Category Total")
        print("6. Search Expense")
        print("7. Set Budget")
        print("8. Budget Status")
        print("9. Sort Expenses")
        print("10. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_expense()
        
        elif choice == 2:
            view_expenses()

        elif choice == 3:
            delete_expenses()

        elif choice == 4:
            show_total()

        elif choice == 5:
            show_category_totals()

        elif choice == 6:
            search_expense()

        elif choice == 7:
            set_budget()

        elif choice == 8:
            budget_status()

        elif choice == 9:
            sort_expenses()

        elif choice == 10:
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
                                
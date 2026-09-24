def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n📋 All Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")


def total_spending(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}")


def category_spending(expenses):
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n📊 Category-wise Spending:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")


def set_budget():
    budget = float(input("Enter monthly budget: "))
    print("✅ Budget set successfully!")
    return budget


def check_budget(expenses, budget):
    total = sum(exp["amount"] for exp in expenses)

    print(f"\n💼 Budget: ₹{budget}")
    print(f"💸 Spent: ₹{total}")

    if total > budget:
        print("⚠️ Budget exceeded!")
    else:
        print(f"✅ Remaining Budget: ₹{budget - total}")


def main():
    expenses = []
    budget = 0

    while True:
        print("\n===== SMART EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Set Budget")
        print("6. Check Budget")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spending(expenses)

        elif choice == "4":
            category_spending(expenses)

        elif choice == "5":
            budget = set_budget()

        elif choice == "6":
            check_budget(expenses, budget)

        elif choice == "7":
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again!")


# Run the program
main()

import json
from datetime import datetime

# -------- Expense Class --------
class Expense:
    def __init__(self, amount, category, note):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return self.__dict__


# -------- Expense Manager --------
class ExpenseManager:
    # FILE = "expenses.json"
    FILE="14_File_Handling/expenses.json"
    def __init__(self):
        try:
            with open(self.FILE, "r") as f:
                self.expenses = json.load(f)
        except:
            self.expenses = []


    def add_expense(self, expense):
        self.expenses.append(expense.to_dict())
        self.save()

    def view_expenses(self):
        for exp in self.expenses:
            print(exp)

    def filter_by_category(self, category):
        for exp in self.expenses:
            if exp["category"].lower() == category.lower():
                print(exp)
        

    def total_expense(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print("Total Expense:", total)

    def monthly_summary(self, month):
        total = 0
        for exp in self.expenses:
            # '2026-08-01' -- EXTRACT MONTH FROM DATE 
            if exp["date"][5:7] == month:
                total += exp["amount"]
        print(f"Total for month {month}:", total)

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.expenses, f, indent=4)


# -------- Demo --------
em = ExpenseManager()

em.add_expense(Expense(200, "Food", "Lunch"))
em.add_expense(Expense(500, "Travel", "Bus pass"))
em.add_expense(Expense(1000, "Bills", "Electricity"))
em.add_expense(Expense(500, "Food", "Dinner"))
em.add_expense(Expense(10000, "Travel", "Trip"))
em.add_expense(Expense(1200, "Bills", "Electricity"))

print("\nAll Expenses:")
em.view_expenses()

print("\nFood Expenses:")
em.filter_by_category("Food")

print("\n")
em.total_expense()

print("\n")

em.monthly_summary("08")  # OCTOBER
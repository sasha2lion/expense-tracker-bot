expenses = []

def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})

def list_expenses():
    return expenses

def total():
    return sum(e["amount"] for e in expenses)

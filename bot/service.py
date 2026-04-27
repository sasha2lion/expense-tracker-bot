expenses = []

def add_expense(name, amount, category="other"):
    expenses.append({
        "name": name,
        "amount": amount,
        "category": category
    })
    expenses.append({"name": name, "amount": amount})

def list_expenses():
    return expenses

def total():
    return sum(e["amount"] for e in expenses)
def format_expenses():
    return [
        f"{e['name']} ({e['category']}) - {e['amount']}"
        for e in expenses
    ]

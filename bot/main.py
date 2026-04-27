# Telegram Expense Tracker Bot (demo version)

expenses = []

def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})

def list_expenses():
    return expenses

def total():
    return sum(e["amount"] for e in expenses)


# имитация команд бота
def handle_command(command):
    parts = command.split()

    if parts[0] == "/add":
        name = parts[1]
        amount = float(parts[2])
        add_expense(name, amount)
        return f"Added: {name} - {amount}"

    elif parts[0] == "/list":
        return "\n".join([f"{e['name']} - {e['amount']}" for e in expenses])

    elif parts[0] == "/total":
        return f"Total: {total()}"

    else:
        return "Unknown command"


if __name__ == "__main__":
    print(handle_command("/add coffee 5"))
    print(handle_command("/add food 10"))
    print(handle_command("/list"))
    print(handle_command("/total"))

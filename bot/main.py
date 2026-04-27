from bot.service import add_expense, list_expenses, total

def handle_command(command):
    parts = command.split()

   if parts[0] == "/add":
    try:
        name = parts[1]
        amount = float(parts[2])
        category = parts[3] if len(parts) > 3 else "other"

        add_expense(name, amount, category)
        return f"Added: {name} - {amount} ({category})"

    except:
        return "Error: use /add name amount category"

    elif parts[0] == "/list":
        return "\n".join([f"{e['name']} - {e['amount']}" for e in list_expenses()])

    elif parts[0] == "/total":
        return f"Total: {total()}"

    return "Unknown command"

try:
    amount = float(parts[2])
except:
    return "Error: use /add name amount"

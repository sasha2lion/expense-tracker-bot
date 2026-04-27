from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "HellenkaBot"

expenses = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает 💰")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.split()
        name = text[1]
        amount = float(text[2])

        expenses.append({"name": name, "amount": amount})

        await update.message.reply_text(f"Добавлено: {name} - {amount}")
    except:
        await update.message.reply_text("Пример: /add кофе 5")

async def list_expenses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not expenses:
        await update.message.reply_text("Нет расходов")
        return

    text = "\n".join([f"{e['name']} - {e['amount']}" for e in expenses])
    await update.message.reply_text(text)

async def total(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total_sum = sum(e["amount"] for e in expenses)
    await update.message.reply_text(f"Итого: {total_sum}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", list_expenses))
app.add_handler(CommandHandler("total", total))

app.run_polling()

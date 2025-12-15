from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("8438442286:AAFDLLAqI1zYgNaCQXZUVlXFNCpOEmBP6F0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Join Channel", url="https://web.telegram.org/a/#-1003465632784")],
        [InlineKeyboardButton("📦 Products", callback_data="products")],
        [InlineKeyboardButton("💬 Support", url="https://t.me/techdealshuby")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Choose an option below 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

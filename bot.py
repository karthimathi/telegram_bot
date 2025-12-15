import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8438442286:AAFDLLAqI1zYgNaCQXZUVlXFNCpOEmBP6F0")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

# 👉 ADD YOUR DETAILS HERE
CHANNEL_USERNAME = "https://t.me/techdealshuby"     # without @
SUPPORT_USERNAME = "@mkarthick1997"        # without @

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_USERNAME}")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Choose an option below 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import schedule
import time
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

bot = Bot(token=BOT_TOKEN)

# 🔹 STATIC AMAZON PRODUCTS
products = [
    {
        "title": "Samsung Galaxy M14 5G",
        "price": "₹12,499",
        "link": "https://www.amazon.in/dp/B0BXD5H6YF?tag=yourtag-21"
    },
    {
        "title": "boAt Rockerz 255 Pro+",
        "price": "₹1,099",
        "link": "https://www.amazon.in/dp/B08TV2P1N8?tag=yourtag-21"
    },
    {
        "title": "Redmi Power Bank 20000mAh",
        "price": "₹2,099",
        "link": "https://www.amazon.in/dp/B07JQ8Q6X6?tag=yourtag-21"
    }
]

def post_product():
    product = random.choice(products)

    text = f"""
🔥 *Amazon Best Pick*

📦 *{product['title']}*
💰 Price: {product['price']}

🛒 Grab it now 👇
"""

    buttons = [
        [InlineKeyboardButton("🛒 Buy on Amazon", url=product["link"])],
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# ⏰ AUTO POST EVERY 3 HOURS
schedule.every(3).hours.do(post_product)

print("Bot started...")

while True:
    schedule.run_pending()
    time.sleep(1)

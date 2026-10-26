import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not configured")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🔥 شحن Free Fire", callback_data="freefire"),
        InlineKeyboardButton("🎮 شحن PUBG Mobile", callback_data="pubg"),
        InlineKeyboardButton("💬 الدعم الفني", callback_data="support")
    )

    bot.send_message(
        message.chat.id,
        "مرحباً بك في Jomaa7Store 🎮\n\n"
        "اختر اللعبة التي تريد شحنها:",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == "freefire":
        text = "🔥 اخترت Free Fire\nسيتم إضافة باقات الألماس قريباً."
    elif call.data == "pubg":
        text = "🎮 اخترت PUBG Mobile\nسيتم إضافة باقات UC قريباً."
    elif call.data == "support":
        text = "💬 للدعم الفني، تواصل مع إدارة المتجر."
    else:
        text = "خيار غير معروف."

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, text)

bot.infinity_polling()

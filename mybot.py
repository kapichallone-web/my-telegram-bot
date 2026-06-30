from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8829434059:AAE0bL50Yr-pSM20mPTVpMuN5OHA-1nvkA0"


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Reply Keyboard
    reply_keyboard = [
        [KeyboardButton("📥 បង្កើតអាខោន")],
        [KeyboardButton("📞 ទំនាក់ទំនង")],
    ]

    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard,
        resize_keyboard=True
    )

    # Inline Buttons
    inline_keyboard = [
        [
            InlineKeyboardButton(
                "📝 ចុះឈ្មោះឥតគិតថ្លៃ",
                url="https://t.me/F7_service",
            )
        ],
        [
            InlineKeyboardButton(
                "📞 ទំនាក់ទំនងផ្នែកបម្រើអតិថិជន",
                url="https://t.me/F7_service",
            )
        ],
    ]

    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    text = (
        "🎉 សូមស្វាគមន៍មកកាន់ F7 Service\n\n"
        "✅ ផ្តល់សេវាកម្ម 24/365\n"
        "✅ បុគ្គលិករហ័ស និងមានវិជ្ជាជីវៈ\n"
        "✅ គាំទ្រអតិថិជនគ្រប់ពេល\n\n"
        "សូមជ្រើសរើសប៊ូតុងខាងក្រោម 👇"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=inline_markup,
    )

    await update.message.reply_text(
        "📌 ឬជ្រើសរើស Menu ខាងក្រោម",
        reply_markup=reply_markup,
    )


# Handle Buttons
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📥 បង្កើតអាខោន":

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉 បង្កើតអាខោន",
                        url="https://t.me/F7_service",
                    )
                ]
            ]
        )

        await update.message.reply_text(
            "ចុចប៊ូតុងខាងក្រោមដើម្បីបង្កើតអាខោន",
            reply_markup=keyboard,
        )

    elif text == "📞 ទំនាក់ទំនង":

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👉 ទំនាក់ទំនង",
                        url="https://t.me/F7_service",
                    )
                ]
            ]
        )

        await update.message.reply_text(
            "ចុចប៊ូតុងខាងក្រោមដើម្បីទំនាក់ទំនង",
            reply_markup=keyboard,
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()

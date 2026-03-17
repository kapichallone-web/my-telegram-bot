from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ១. ដាក់លេខ Token ដែលអ្នកបានពី BotFather នៅទីនេះ
TOKEN = '7836805540:AAFZFfe3HJz647PKFwaWXncfTOiBghKD44Y'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # រូបភាព (Link រូបភាព ឬ File ID)
    photo_url = "https://i.postimg.cc/BvvJywph/1.png" 
    
    # អត្ថបទស្វាគមន៍ (ដូចក្នុងរូបភាពរបស់អ្នក)
    welcome_text = (
        "J8BET ឧត្តមភាពក្នុងការផ្តល់សេវាកូនអតិថិជន 24/365\n"
        "ផ្តល់ជូនសេវាកម្មដោយបុគ្គលិកដែលមានវិជ្ជាជីវៈ រហ័ស...\n\n"
        "ចុះឈ្មោះថ្ងៃនេះទទួលបានទឹកប្រាក់ $8 ភ្លាមៗ"
    )

    # បង្កើតប៊ូតុង (Buttons)
    keyboard = [
        [InlineKeyboardButton("ចុះឈ្មោះឥតគិតថ្លៃឡូវនេះ 📝", url="https://t.me/j8bet_live01")],
        [InlineKeyboardButton("ដោះស្រាយបញ្ហាប្រើប្រាស់អតិថិជន 📞", url="https://t.me/j8bet_live01")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ផ្ញើរូបភាពជាមួយអត្ថបទ និងប៊ូតុង
    await update.message.reply_photo(
        photo=photo_url,
        caption=welcome_text,
        reply_markup=reply_markup
    )

def main():
    # បង្កើត Application
    application = Application.builder().token(TOKEN).build()

    # នៅពេលអ្នកប្រើចុច /start
    application.add_handler(CommandHandler("start", start))

    # ដំណើរការ Bot
    print("Bot កំពុងដើរ...")
    application.run_polling()

if __name__ == '__main__':
    main()
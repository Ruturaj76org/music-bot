from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .handlers import start, handle_search

def main():
    app = Application.builder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search))

    app.run_polling()

if __name__ == "__main__":
    main()

import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .handlers import start, handle_search
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_TOKEN not found in environment variables!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search))
    
    # Start polling and ensure no multiple processes
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()



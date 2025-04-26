import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .handlers import start, handle_search
import time

def main():
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_TOKEN not found in environment variables!")

    app = Application.builder().token(token).build()

    # Adding handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search))

    # Adding a retry mechanism with a short delay in case of errors
    retry_attempts = 5
    for attempt in range(retry_attempts):
        try:
            app.run_polling()
            break
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(5)  # wait before retrying

if __name__ == "__main__":
    main()

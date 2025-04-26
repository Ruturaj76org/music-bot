from telegram import Update
from telegram.ext import CallbackContext
from .downloader import search_and_download
from .utils import create_buttons
from .constants import BUTTONS

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome! Send me a song name, and I'll fetch it for you.",
        reply_markup=create_buttons(BUTTONS)
    )

async def handle_search(update: Update, context: CallbackContext):
    query = update.message.text
    result = await search_and_download(query)
    if result:
        await update.message.reply_audio(
            audio=result['file'],
            title=result['title'],
            performer=result['artist'],
            caption=f"{result['title']} by {result['artist']}",
            reply_markup=create_buttons(BUTTONS)
        )
    else:
        await update.message.reply_text("Sorry, I couldn't find that song.")

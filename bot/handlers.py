from telegram import Update
from telegram.ext import CallbackContext
from .downloader import search_and_download
from .utils import build_message
from .constants import BUTTONS, STATUS_MESSAGES

async def start(update: Update, context: CallbackContext):
    """Handle the /start command."""
    await update.message.reply_text(
        "Welcome! Send me the song name, and I'll fetch it for you.",
    )

async def handle_search(update: Update, context: CallbackContext):
    """Handle song name input, fetch details, and show response."""
    query = update.message.text
    await update.message.reply_text(STATUS_MESSAGES["fetching_details"])

    result = await search_and_download(query)
    if result:
        context.user_data['song_data'] = result  # <-- Store song for later use

        message_data = build_message(
            result['title'],
            result['artist'],
            result['thumbnail'],
            STATUS_MESSAGES["song_found"],
            BUTTONS
        )

        await update.message.reply_photo(
            photo=message_data['photo'],
            caption=message_data['caption'],
            reply_markup=message_data['reply_markup'],
            parse_mode="Markdown"  # <-- Enable markdown for bold title
        )
    else:
        await update.message.reply_text(STATUS_MESSAGES["song_not_found"])

async def button_callback(update: Update, context: CallbackContext):
    """Handle button presses (Get song or Not found)."""
    query = update.callback_query
    data = query.data

    if data == "get_song":
        song_data = context.user_data.get('song_data')
        if song_data:
            await query.message.reply_audio(
                audio=song_data['file'],
                caption=f"Here is your song: {song_data['title']} by {song_data['artist']}",
            )
        else:
            await query.message.reply_text("No song data available.")

    elif data == "not_found":
        await query.message.reply_text("Can you give me more details? Try including artist or album.")

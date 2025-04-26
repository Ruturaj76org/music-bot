# bot/utils.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_buttons(buttons):
    """Creates inline buttons for the bot response."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text=buttons["get_song"], callback_data="get_song")],
        [InlineKeyboardButton(text=buttons["not_found"], callback_data="not_found")]
    ])

def build_message(title, artist, thumbnail_url, status_message, buttons):
    """Constructs a message with song details, thumbnail, and buttons."""
    return {
        "caption": f"**{title}** by {artist}",
        "photo": thumbnail_url,
        "text": status_message,
        "reply_markup": create_buttons(buttons)
    }

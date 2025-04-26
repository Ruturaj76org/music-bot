from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_buttons(buttons):
    keyboard = [
        [InlineKeyboardButton(text=buttons["get_song"], callback_data="get_song")],
        [InlineKeyboardButton(text=buttons["not_found"], callback_data="not_found")]
    ]
    return InlineKeyboardMarkup(keyboard)

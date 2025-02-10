"""Executes and runs the Telegram bot"""

import os
import logging
import logic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (ApplicationBuilder, ContextTypes,
                          CommandHandler, Updater, CallbackQueryHandler)
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the number of reactions required
REQUIRED_REACTIONS = 1 # for production, this should be 4
current_reactions = 0
player_names = []
# Store user reactions in a dictionary
user_reactions = {}

def reset_reactions():
    global current_reactions, players, user_reactions
    current_reactions = 0
    player_names = []
    user_reactions = {}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Command to start the game"""
    keyboard = [
        [InlineKeyboardButton("Ready", callback_data='react')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Waiting for players...!', reply_markup=reply_markup)

# Callback query handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_reactions
    query = update.callback_query
    await query.answer()

    if query.data == 'react':
        user_id = query.from_user.id

        # Count reactions per user
        user_reactions[user_id] = user_reactions.get(user_id, 0) + 1
        player_names.append(query.from_user.first_name)

        # Generate text for insertion into message
        players_text = "\n".join(players_names)

        if user_reactions[user_id] == 1:
            current_reactions += 1
            await query.edit_message_text(text=f"{current_reactions}/{REQUIRED_REACTIONS} players ready:\n\n"
                                               f"{players_text}")

            # Check if we've reached the required number of reactions
            if current_reactions >= REQUIRED_REACTIONS:
                tiles = '\n'.join([''.join(sublist) for sublist in logic.deal_tiles()])

                await query.message.reply_text(f"Starting game! Hands dealt...\n\n"
                                               f"{tiles}")
                # Reset the counter - should be done at the end of the game
                # reset_reactions()

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    # Register command and callback handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import motor.motor_asyncio
from database.users_chats_db import db

# Command to Send Vote Messa
@Client.on_callback_query()
async def button_click(client, callback_query: CallbackQuery):
    emoji = callback_query.data  # Retrieve the clicked emoji from callback data

    # Check if votes are initialized; if not, initialize them
    votes = await db.get_votes()
    if not votes:
        await db.initialize_votes()
        votes = {emoji: 0 for emoji in ["🤬", "👎", "🖕", "🤡", "💩", "👽"]}

    # Update the vote count for the clicked emoji
    await db.update_vote(emoji)

    # Fetch updated vote counts
    votes = await db.get_votes()

    # Create updated buttons
    buttons = [
        [
            InlineKeyboardButton(f"🤬: {votes['🤬']}", callback_data="🤬"),
            InlineKeyboardButton(f"👎: {votes['👎']}", callback_data="👎"),
            InlineKeyboardButton(f"🖕: {votes['🖕']}", callback_data="🖕"),
            InlineKeyboardButton(f"🤡: {votes['🤡']}", callback_data="🤡"),
            InlineKeyboardButton(f"💩: {votes['💩']}", callback_data="💩"),
            InlineKeyboardButton(f"👽: {votes['👽']}", callback_data="👽"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    # Edit the message with updated vote counts
    await callback_query.message.edit_reply_markup(reply_markup=reply_markup)
    await callback_query.answer("Vote counted!")

# Callback Query Handler for Button Clicks
# @Client.on_callback_query()
# async def button_click(client, callback_query: CallbackQuery):
#     emoji = callback_query.data  # Retrieve the clicked emoji from callback data
#     await db.update_vote(emoji)  # Update the vote count in the database

#     # Fetch updated vote counts
#     votes = await db.get_votes()

#     # Create updated buttons
#     buttons = [
#         [
#             InlineKeyboardButton(f"🤬: {votes['🤬']}", callback_data="🤬"),
#             InlineKeyboardButton(f"👎: {votes['👎']}", callback_data="👎"),
#             InlineKeyboardButton(f"🖕: {votes['🖕']}", callback_data="🖕"),
#             InlineKeyboardButton(f"🤡: {votes['🤡']}", callback_data="🤡"),
#             InlineKeyboardButton(f"💩: {votes['💩']}", callback_data="💩"),
#             InlineKeyboardButton(f"👽: {votes['👽']}", callback_data="👽"),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(buttons)

#     # Edit the message with updated vote counts
#     await callback_query.message.edit_reply_markup(reply_markup=reply_markup)
#     await callback_query.answer("Vote counted!")



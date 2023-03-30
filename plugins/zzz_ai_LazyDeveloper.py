from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from info import *
from utils import lazy_answer
import openai
openai.api_key = OPENAI_API


@Client.on_message(filters.group & filters.text & filters.incoming)
async def run_ai(client, message):
    k = await lazy_answer(client, message)
    if k == False:
        return

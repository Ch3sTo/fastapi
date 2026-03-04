import asyncio

import requests
import dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
dotenv.load_dotenv()
token=os.getenv("token")
bot=Bot(token)
ds=Dispatcher()
@ds.message(Command("hi"))
async def hello(msg:Message):
    data=(requests.get("http://127.0.0.1:8000/")).json()
    await msg.answer(data["message"])
async def start():
    await ds.start_polling(bot)
asyncio.run(start())
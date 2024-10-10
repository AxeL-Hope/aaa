import json
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (Message, InlineKeyboardMarkup,
                           InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton)

authBotToken = f"7308514421:AAHb3dBSkReBU2MgK7O50f057HPIqaMlLQ4"

# Настройка параметров
storage = MemoryStorage()
bot = Bot(token=authBotToken)
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"{message.chat.id}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot, skip_updates=True)

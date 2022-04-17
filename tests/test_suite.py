import pytest
import aiogram
from aiotests import AiogramTestingSuite
import os

bot = aiogram.Bot(token=os.getenv("TEST_BOT_TOKEN"), parse_mode="HTML")
dp = aiogram.Dispatcher(bot)
suite = AiogramTestingSuite(lambda: bot, lambda: dp)

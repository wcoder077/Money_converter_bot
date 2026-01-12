from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from config import Config, load_config
from models.postgresql import Database

config: Config = load_config()

bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode="HTML"))

db = Database()

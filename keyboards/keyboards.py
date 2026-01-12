from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushurish."),
        BotCommand(
            command="taklif",
            description="Bot masalasi bo'yicha dasturchiga taklif yoki shikoyat. ",
        ),
    ]
    await bot.set_my_commands(commands)


base = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="💸 Barcha pul birliklarni | UZB so'miga | taqqoslab ko'rish"
            ),
        ],
        [
            KeyboardButton(text="🧮 Pul birligi Kalkulatori"),
            KeyboardButton(text="🏠 Asosiy menu"),
        ],
    ],
    resize_keyboard=True,
)


kurs_btns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 orqaga"),
        ],
        [
            KeyboardButton(text="🇺🇸 USD"),
            KeyboardButton(text="🇪🇺 EUR"),
            KeyboardButton(text="🇷🇺 RUB"),
            KeyboardButton(text="🇺🇿 UZS"),
        ],
        [
            KeyboardButton(text="🇯🇵 JPY"),
            KeyboardButton(text="🇬🇧 GBP"),
            KeyboardButton(text="🇨🇳 CNY"),
            KeyboardButton(text="🇦🇪 AED"),
        ],
        [
            KeyboardButton(text="🇹🇷 TRY"),
            KeyboardButton(text="🇰🇿 KZT"),
            KeyboardButton(text="🇰🇬 KGS"),
            KeyboardButton(text="🇨🇭 CHF"),
        ],
        [
            KeyboardButton(text="🇨🇦 CAD"),
            KeyboardButton(text="🇦🇺 AUD"),
            KeyboardButton(text="🇸🇪 SEK"),
            KeyboardButton(text="🇳🇴 NOK"),
        ],
        [
            KeyboardButton(text="🇩🇰 DKK"),
            KeyboardButton(text="🇵🇱 PLN"),
            KeyboardButton(text="🇮🇳 INR"),
            KeyboardButton(text="🇵🇰 PKR"),
        ],
        [
            KeyboardButton(text="🇧🇩 BDT"),
            KeyboardButton(text="🇭🇰 HKD"),
            KeyboardButton(text="🇸🇬 SGD"),
            KeyboardButton(text="🇲🇾 MYR"),
        ],
        [
            KeyboardButton(text="🇹🇭 THB"),
            KeyboardButton(text="🇰🇷 KRW"),
            KeyboardButton(text="🇹🇼 TWD"),
            KeyboardButton(text="🇸🇦 SAR"),
        ],
        [
            KeyboardButton(text="🇶🇦 QAR"),
            KeyboardButton(text="🇰🇼 KWD"),
            KeyboardButton(text="🇧🇭 BHD"),
            KeyboardButton(text="🇯🇴 JOD"),
        ],
        [
            KeyboardButton(text="🇪🇬 EGP"),
            KeyboardButton(text="🇧🇷 BRL"),
            KeyboardButton(text="🇳🇿 NZD"),
            KeyboardButton(text="🇨🇱 CLP"),
        ],
    ],
    resize_keyboard=True,
)

cur_codes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 orqaga"),
            KeyboardButton(text="🔄 qayta"),
        ],
        [
            KeyboardButton(text="🇺🇸 USD"),
            KeyboardButton(text="🇪🇺 EUR"),
            KeyboardButton(text="🇷🇺 RUB"),
            KeyboardButton(text="🇺🇿 UZS"),
        ],
        [
            KeyboardButton(text="🇯🇵 JPY"),
            KeyboardButton(text="🇬🇧 GBP"),
            KeyboardButton(text="🇨🇳 CNY"),
            KeyboardButton(text="🇦🇪 AED"),
        ],
        [
            KeyboardButton(text="🇹🇷 TRY"),
            KeyboardButton(text="🇰🇿 KZT"),
            KeyboardButton(text="🇰🇬 KGS"),
            KeyboardButton(text="🇨🇭 CHF"),
        ],
        [
            KeyboardButton(text="🇨🇦 CAD"),
            KeyboardButton(text="🇦🇺 AUD"),
            KeyboardButton(text="🇸🇪 SEK"),
            KeyboardButton(text="🇳🇴 NOK"),
        ],
        [
            KeyboardButton(text="🇩🇰 DKK"),
            KeyboardButton(text="🇵🇱 PLN"),
            KeyboardButton(text="🇮🇳 INR"),
            KeyboardButton(text="🇵🇰 PKR"),
        ],
        [
            KeyboardButton(text="🇧🇩 BDT"),
            KeyboardButton(text="🇭🇰 HKD"),
            KeyboardButton(text="🇸🇬 SGD"),
            KeyboardButton(text="🇲🇾 MYR"),
        ],
        [
            KeyboardButton(text="🇹🇭 THB"),
            KeyboardButton(text="🇰🇷 KRW"),
            KeyboardButton(text="🇹🇼 TWD"),
            KeyboardButton(text="🇸🇦 SAR"),
        ],
        [
            KeyboardButton(text="🇶🇦 QAR"),
            KeyboardButton(text="🇰🇼 KWD"),
            KeyboardButton(text="🇧🇭 BHD"),
            KeyboardButton(text="🇯🇴 JOD"),
        ],
        [
            KeyboardButton(text="🇪🇬 EGP"),
            KeyboardButton(text="🇧🇷 BRL"),
            KeyboardButton(text="🇳🇿 NZD"),
            KeyboardButton(text="🇨🇱 CLP"),
        ],
    ],
    resize_keyboard=True,
)

currency = [
    "🇺🇸 USD",
    "🇪🇺 EUR",
    "🇬🇧 GBP",
    "🇺🇿 UZS",
    "🇯🇵 JPY",
    "🇷🇺 RUB",
    "🇨🇳 CNY",
    "🇦🇪 AED",
    "🇹🇷 TRY",
    "🇰🇿 KZT",
    "🇰🇬 KGS",
    "🇨🇭 CHF",
    "🇨🇦 CAD",
    "🇦🇺 AUD",
    "🇸🇪 SEK",
    "🇳🇴 NOK",
    "🇩🇰 DKK",
    "🇵🇱 PLN",
    "🇮🇳 INR",
    "🇵🇰 PKR",
    "🇧🇩 BDT",
    "🇭🇰 HKD",
    "🇸🇬 SGD",
    "🇲🇾 MYR",
    "🇹🇭 THB",
    "🇰🇷 KRW",
    "🇹🇼 TWD",
    "🇸🇦 SAR",
    "🇶🇦 QAR",
    "🇰🇼 KWD",
    "🇧🇭 BHD",
    "🇯🇴 JOD",
    "🇪🇬 EGP",
    "🇲🇦 MAD",
    "🇿🇦 ZAR",
    "🇧🇷 BRL",
    "🇲🇽 MXN",
    "🇦🇷 ARS",
    "🇨🇱 CLP",
    "🇳🇿 NZD",
]

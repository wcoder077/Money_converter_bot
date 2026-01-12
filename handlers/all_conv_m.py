import datetime
import requests

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from keyboards.keyboards import currency, kurs_btns, base
from handlers.calculator_cur import format_money

router: Router = Router()


@router.message(F.text == "💸 Barcha pul birliklarni | UZB so'miga | taqqoslab ko'rish")
async def process_any_message(message: Message):
    API_KEY = "c1ce472c6f30b056ba994142"
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS"
    res = requests.get(URL)
    rate = res.json()["conversion_rate"]

    await message.answer(text="Tanlashingiz mumkin!", reply_markup=kurs_btns)


@router.message(F.text == "🔙 orqaga")
async def back_f(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b>◀️Qaytdi..</b>", reply_markup=base, parse_mode="HTML")


@router.message(F.text == "🏠 Asosiy menu")
async def back_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Asosiy menuga qaytdingiz, birorta pul birligini ko'rmoqchimisz? Agar /start bosing!",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(F.text.in_(currency))
async def process_any_message(message: Message):
    currency_code = message.text.split()[-1]
    API_KEY = "c1ce472c6f30b056ba994142"
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency_code}/UZS"
    res = requests.get(URL)

    if res.status_code == 200:
        timestamp = res.json()["time_last_update_utc"]
        rate = res.json()["conversion_rate"]

        caption = (
            f"<blockquote>Updated-time: {timestamp[:-6]}</blockquote>\n\n"
            f"<b><i>①{currency_code} ➜ UZS:</i></b> {format_money(rate)}\n"
        )
        await message.answer(text=caption, parse_mode="HTML")
    else:
        await message.answer("Xatolik yuz berdi!")

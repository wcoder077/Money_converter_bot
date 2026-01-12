from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import requests
from keyboards.keyboards import base

router: Router = Router()


@router.message(CommandStart())
async def start_f(message: Message):
    await message.answer(
        text="""
Assalomu alaykum! 👋

Bu bot valyutalarni kursdan kursga o‘girib, bir valyutadan boshqa valyutaga *osonlik bilan konvertatsiya qilish* imkonini beradi. 💱

Foydalari:
- Alohida dastur yoki kalkulyator kerak emas.
- Faqat botga kirish kifoya, va siz darhol kerakli valyutani hisoblab olasiz.

Shunchaki kirib, oson va tez valyutalarni konvertatsiya qiling! 🚀
""",
        reply_markup=base,
        parse_mode="Markdown",
    )

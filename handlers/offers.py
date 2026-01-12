from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import base
from states.states import OfferState

GROUP_ID = -1003283765837

router = Router()


@router.message(Command("taklif"))
async def start_offer(message: Message, state: FSMContext):
    await state.set_state(OfferState.offer)
    await message.answer("📝 Shikoyat yoki taklifingizni yozing 👇")


@router.message(OfferState.offer)
async def send_offer(message: Message, state: FSMContext):
    if message.chat.type != "private":
        return

    text = (
        f"<blockquote>📩 Yangi taklif\n</blockquote>"
        f"<i>Fullname: {message.from_user.full_name}\nUsername: @{message.from_user.username}\n\n</i>"
        # f"🆔 {message.from_user.id}\n\n"
        f"💬 <blockquote>{message.text}</blockquote>"
    )

    await message.bot.send_message(GROUP_ID, text, parse_mode="HTML")
    await message.answer(
        "<blockquote>Sizni xabaringiz qabul qilindi ✅</blockquote>\nShikoyat va Takliflaringizni inobatga olamiz tashakkur🤝",
        reply_markup=base,
    )
    await message.answer("Botdan foydalanishingiz mumkin👇", reply_markup=base)

    await state.clear()

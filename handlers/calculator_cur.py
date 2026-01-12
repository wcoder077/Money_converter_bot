import requests

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from states.states import ConvertState
from keyboards.keyboards import cur_codes, base

API_KEY = "c1ce472c6f30b056ba994142"

router: Router = Router()


# Pul raqamlarini tushunarli qilish
def format_money(amount: int | float) -> str:
    return f"{amount:,.0f}".replace(".", ",")


@router.message(F.text == "🔄 qayta", ConvertState.to_cur)
async def back_to_from(message: Message, state: FSMContext):
    await state.set_state(ConvertState.from_cur)
    await message.answer("1-pul birligini qayta kiriting...", reply_markup=cur_codes)


@router.message(F.text == "🔙 orqaga")
async def back_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("<b>◀️Qaytdi</b>", reply_markup=base, parse_mode="HTML")


#################################################################


@router.message(F.text == "🧮 Pul birligi Kalkulatori")
async def start_calc(message: Message, state: FSMContext):
    await state.set_state(ConvertState.from_cur)
    await message.answer(
        text="Pul birligi kalkulatorni ishlatish uchun \n⬇️ quyidagi ishlarni ketma ketlik bilan bajaring..."
    )
    await message.reply(text="1-pul birligini kiriting...", reply_markup=cur_codes)


@router.message(ConvertState.from_cur)
async def step_from_cur(message: Message, state: FSMContext):
    await state.update_data(from_cur=message.text.upper())
    await state.set_state(ConvertState.to_cur)

    await message.reply(text="2-pul birligini kiriting...", reply_markup=cur_codes)


@router.message(ConvertState.to_cur)
async def step_to_cur(message: Message, state: FSMContext):
    await state.update_data(to_cur=message.text.upper())
    await state.set_state(ConvertState.how_much)
    await message.answer(
        text="<blockquote>Qancha summani convertatsiya qilasiz?</blockquote>\n<b><i>Kiriting:</i></b>",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML",
    )


@router.message(ConvertState.how_much)
async def step_how_much(message: Message, state: FSMContext):
    try:
        how_much = float(message.text)
    except ValueError:
        await message.reply("Iltimos, faqat son kiriting!")
        return

    await state.update_data(how_much=how_much)

    data = await state.get_data()
    from_cur = data["from_cur"]
    to_cur = data["to_cur"]

    # Fixed extraction
    from_code = from_cur.split()[-1]
    to_code = to_cur.split()[-1]

    if from_code != to_code:
        URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_code}/{to_code}"
        res = requests.get(URL)

        if res.status_code == 200:
            json_data = res.json()
            if json_data["result"] == "success":
                rate = json_data["conversion_rate"]
                timestamp = json_data["time_last_update_utc"]
                result = how_much * rate

                caption = (
                    f"<blockquote>Updated-time: {timestamp[:-6]}</blockquote>\n\n"
                    f"<b><i>{format_money(how_much)} {from_code} ➜ {to_code}:</i></b> {format_money(result)}"
                )
                await message.answer(text=caption, parse_mode="HTML", reply_markup=base)
            else:
                await message.answer(
                    f"API xatolik: {json_data.get('error-type', 'Noma\'lum')}"
                )
        else:
            await message.answer("Internet ulanmadi yoki API cheklangan!")

        await state.clear()
    else:
        await message.answer("Iltimos, 2 xil pul birligini kiriting!")

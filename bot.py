import asyncio
import logging

from aiogram import Dispatcher

from handlers import start, calculator_cur, offers, all_conv_m

from loader import bot, db

from keyboards.keyboards import set_commands

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
    )
    logger.info("Starting bot")

    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        start.router, offers.router, calculator_cur.router, all_conv_m.router
    )

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

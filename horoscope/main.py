import asyncio
import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from  handlers import router, bot

async def main():
    telebot = bot
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await telebot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(telebot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
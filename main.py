import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Merhaba {message.from_user.first_name}, bot çalışıyor ✅")

async def main():
    print("Bot başlatılıyor...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

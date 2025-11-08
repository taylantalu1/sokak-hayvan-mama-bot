from aiogram import Bot, Dispatcher, types
import asyncio

API_TOKEN = "BOT_TOKENINIZI_BURAYA_YERLESTIRIN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Mesajın: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

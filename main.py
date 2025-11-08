from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from keep_alive import keep_alive
import json
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# JSON verisi
with open("data/noktalar.json", "r", encoding="utf-8") as f:
    noktalar = json.load(f)

# Başlangıç ve yardım
@dp.message_handler(commands=['start', 'yardim'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Merhaba! 🐾\n"
        "/listele - Mama noktalarını göster\n"
        "/yardim - Bu yardım mesajını göster"
    )

# Noktaları listele
@dp.message_handler(commands=['listele'])
async def noktalar_goster(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    for i, nokta in enumerate(noktalar):
        keyboard.add(InlineKeyboardButton(
            text=nokta['yer'],
            callback_data=f"konum_{i}"
        ))
    await message.reply("Mama noktaları:", reply_markup=keyboard)

# Konum gönderme
@dp.callback_query_handler(lambda c: c.data.startswith('konum_'))
async def konum_gonder(callback_query: types.CallbackQuery):
    index = int(callback_query.data.split('_')[1])
    nokta = noktalar[index]

    mesaj = f"📍 {nokta['yer']}\n{nokta.get('aciklama','')}"
    if nokta.get('foto'):
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=nokta['foto'], caption=mesaj)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text=mesaj)

    # Konum varsa gönder
    if 'lat' in nokta and 'lon' in nokta:
        await bot.send_location(
            chat_id=callback_query.from_user.id,
            latitude=nokta['lat'],
            longitude=nokta['lon']
        )

# Botu çalıştır
if __name__ == "__main__":
    keep_alive()
    executor.start_polling(dp, skip_updates=True)

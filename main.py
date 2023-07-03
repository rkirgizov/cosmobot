import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def process_start_command(message: types.Message):
        await message.reply("Привет!\nНапиши мне что-нибудь!")
    
@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")
    
@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
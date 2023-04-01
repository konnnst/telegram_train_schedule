from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from apikey import TELEGRAM_API
from rasp import strTrains

HELP = """
<b>/start</b> -- запуск бота
<b>/help</b> -- помощь
➡ -- из Питера в Универ
⬅ -- из Универа в Питер
"""

bot = Bot(TELEGRAM_API)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1, b2, b3 = KeyboardButton('➡️'), KeyboardButton('⬅️'), KeyboardButton('/help')
kb.insert(b1).insert(b2)
kb.add(b3)

@dp.message_handler(commands=['help'])
async def commandHelp(message: types.Message):
    await bot.send_message(message.chat.id, text = HELP, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['start'])
async def commandStart(message: types.Message):
    await message.answer(text = 'Привет дорогой друг!', reply_markup=kb)
    await message.delete()

@dp.message_handler()
async def messageProcess(message: types.Message):
    if message.text == '➡️':
        await message.answer(strTrains(1), parse_mode='HTML')
    elif message.text == '⬅️':
        await message.answer(strTrains(0), parse_mode='HTML')
    else:
        await message.answer('❗ACHTUNG❗WRONG❗COMMAND❗')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
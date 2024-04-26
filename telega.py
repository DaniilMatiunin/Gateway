from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tg_bot_token='6997183606:AAFt1ReIsu-6EjPMPk2zv4Wo8hGaixnDQk8'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message)
    await message.reply("Привет")


@dp.message_handler(commands=["order"])
async def start_command(message: types.Message):
    await message.reply("Наш сайт:... Номер телефона:...")

@dp.message_handler(commands=["menu"])
async def start_command(message: types.Message):
    await message.reply("Горячие блюда :..."
                        "Закуски: ..."
                        )





executor.start_polling(dp)
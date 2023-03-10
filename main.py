from aiogram import Bot, Dispatcher, executor, types
from KEY import TOKEN_API
from command import HELP_COMMAND, DESCRIPTION
import string, random
#бот - сервер который взаимодействует с API Telegram

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands='description')
async def desc_command(message: types.Message):
    await message.answer(DESCRIPTION)
    await message.delete()

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply('<em>Привет добро пожаловать в наш бот</em>', parse_mode='HTML')

@dp.message_handler(commands='give')
async def sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIFSJkC1dNzNFy3pPkrHD2O3PHngegewACIyoAAiMh6Eh3KZjUKlyPkC8E')
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp)
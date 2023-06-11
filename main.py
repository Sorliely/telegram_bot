from aiogram import Bot, Dispatcher, executor, types
from KEY import TOKEN_API
from command import *
from button import *
from random import randrange

# бот - сервер который взаимодействует с API Telegram

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

key_board1 = key_board
inline_board.add(inline_button1, inline_button2)
board_description.add(inline_description)


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=DESCRIPTION,
                           parse_mode='HTML',
                           reply_markup=board_description)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text='Добро пожаловать в наш бот',
                           parse_mode='HTML',
                           reply_markup=key_board)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML', )
    await message.delete()


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://img3.akspic.ru/previews/5/5/4/1/7/171455/171455-zhivopis-illustracia-art-voda-oblako-500x.jpg', )
    await message.delete()


@dp.message_handler(commands=['locetion'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=randrange(1, 100),
                            latitude=randrange(1, 100))
    await message.delete()


@dp.message_handler(commands=['heart'])
async def send_cat(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJO8tkf40M6l1BHQFyM7Oog70pKnaZQQAC-msAAuCjggc43v31Erg32S8E")
    await message.delete()


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://hochusvalit.com/images/Statya8/rabochayavizavyaponiyu.jpeg",
                         caption="Нравится ли тебе данная фотография?",
                         reply_markup=inline_board)


@dp.callback_query_handler()
async def vote_callsback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text="Тебе понравиласт картинка")
    await callback.answer(text="Ну так уйди от сюда")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

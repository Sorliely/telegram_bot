from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

key_board = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_help = KeyboardButton('/help')
button_description = KeyboardButton('/description')
button_photo = KeyboardButton('/photo')
button_vote = KeyboardButton('/vote')
button_heart = KeyboardButton('/heart')

inline_board = InlineKeyboardMarkup(row_width=2)
inline_button1 = InlineKeyboardButton(text='Нравится',
                                      callback_data='like')
inline_button2 = InlineKeyboardButton(text='Не нравится',
                                      callback_data='dislike')

board_description = InlineKeyboardMarkup(row_width=1)
inline_description = InlineKeyboardButton(text='Мой GitHub',
                                          url='https://github.com/Sorliely')

key_board.add(button_help). \
    insert(button_description). \
    insert(button_photo). \
    add(button_vote). \
    insert(button_heart)

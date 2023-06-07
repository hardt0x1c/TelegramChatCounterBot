from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

start_button = [
    [KeyboardButton(text='Начать анализ.')]
]
start_button = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True)

back_menu = [
    [InlineKeyboardButton(text='В главное меню.', callback_data='back_menu')]
]
back_menu = InlineKeyboardMarkup(inline_keyboard=back_menu)

menu = [
    [KeyboardButton(text='Все сообщения', callback_data='all_messages'),
     KeyboardButton(text='Сообщения по дням', callback_data='data_day'),
     KeyboardButton(text='Сообщения по часам', callback_data='data_hour'),
     KeyboardButton(text='Сообщения по месяцам', callback_data='month_data'),
     KeyboardButton(text='Сообщения по годам', callback_data='year_data')],
    [KeyboardButton(text='Кол-во стикеров', callback_data='sticker_data'),
     KeyboardButton(text='Кол-во голосовых', callback_data='voice_data'),
     KeyboardButton(text='Кол-во видеосообщений', callback_data='video_message_data'),
     KeyboardButton(text='Кол-во видео', callback_data='video_file_data'),
     KeyboardButton(text='Кол-во фотографий', callback_data='photo_data')]
]
menu = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True)

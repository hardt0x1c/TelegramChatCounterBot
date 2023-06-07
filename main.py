import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Text
from config import token
import messages as msg
import keyboards as kb
import TelegramScript as TS

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher()


class States(StatesGroup):
    get_file = State()
    get_first_user = State()
    get_second_user = State()
    get_analyze = State()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(msg.greet)
    await message.answer(msg.help_text, reply_markup=kb.start_button)


@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.answer(msg.help_text, reply_markup=kb.back_menu)


@dp.message(Text('Начать анализ.'))
async def start_analyze(message: types.Message, state: FSMContext):
    await state.set_state(States.get_file)
    await message.answer(msg.start_analyze_text, reply_markup=ReplyKeyboardRemove())
    await message.answer('Либо можете вернуться в главное меню.', reply_markup=kb.back_menu)


@dp.message(States.get_file)
async def get_first_nickname(message: types.Message, state: FSMContext):
    await state.set_state(States.get_first_user)
    await bot.download(
        message.document,
        destination='addons/downloads/test.json'
    )
    await message.answer('Введите никнейм первого собеседника.', reply_markup=kb.back_menu)


@dp.message(States.get_first_user)
async def get_second_nickname(message: types.Message, state: FSMContext):
    await state.set_state(States.get_second_user)
    await state.update_data(user1=message.text)
    await message.answer('Введите никнейм второго собеседника.', reply_markup=kb.back_menu)


@dp.message(States.get_second_user)
async def analyze(message: types.Message, state: FSMContext):
    await state.update_data(user2=message.text)
    await state.set_state(States.get_analyze)
    await message.answer(msg.choose_stat, reply_markup=kb.menu)
    await message.answer('Выйти в главное меню.', reply_markup=kb.back_menu)


@dp.message(Text('Все сообщения'), States.get_analyze)
async def all_messages(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.all_messages(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.all_messages(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.message(Text('Сообщения по дням'), States.get_analyze)
async def send_messages_day(message: types.Message):
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.date_day(file)[1])
    await message.answer_photo(photo)
    await message.answer(TS.date_day(file)[0], reply_markup=kb.back_menu)


@dp.message(Text('Сообщения по часам'), States.get_analyze)
async def send_messages_hour(message: types.Message):
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.date_hour(file)[1])
    await message.answer_photo(photo)
    await message.answer(TS.date_hour(file)[0], reply_markup=kb.back_menu)


@dp.message(Text('Сообщения по месяцам'), States.get_analyze)
async def send_messages_month(message: types.Message):
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.month_data(file)[1])
    await message.answer_photo(photo)
    await message.answer(TS.month_data(file)[0], reply_markup=kb.back_menu)


@dp.message(Text('Сообщения по годам'), States.get_analyze)
async def send_messages_year(message: types.Message):
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.year_data(file)[1])
    await message.answer_photo(photo)
    await message.answer(TS.year_data(file)[0], reply_markup=kb.back_menu)


@dp.message(Text('Кол-во стикеров'), States.get_analyze)
async def send_sticker(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.sticker_data(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.sticker_data(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.message(Text('Кол-во голосовых'), States.get_analyze)
async def send_voice(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.voice_data(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.voice_data(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.message(Text('Кол-во видеосообщений'), States.get_analyze)
async def send_video_messages(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.video_message_data(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.video_message_data(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.message(Text('Кол-во видео'), States.get_analyze)
async def send_video(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.video_file_data(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.video_file_data(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.message(Text('Кол-во фотографий'), States.get_analyze)
async def send_photos(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user1 = data.get('user1')
    user2 = data.get('user2')
    name_json = 'addons/downloads/test.json'
    file = TS.load_json(name_json)
    photo = FSInputFile(TS.photo_data(file, user1, user2)[1])
    await message.answer_photo(photo)
    await message.answer(TS.photo_data(file, user1, user2)[0], reply_markup=kb.back_menu)


@dp.callback_query(Text('back_menu'))
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.message.answer('Главное меню:', reply_markup=kb.start_button)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())

from aiogram.types import Message,ReplyKeyboardMarkup
from loader import dp
from keyboards.default.markups import settings,questions,orders
from keyboards.default.markups import catalog,balance,cart,delivery_status
from filters import IsAdmin,IsUser


@dp.message_handler(IsAdmin(),commands=['menu'])
async def admin_menu(message:Message):
    markup = ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
    markup.add(settings)
    markup.row(questions,orders)
    await message.answer(text="Menu",reply_markup=markup)

@dp.message_handler(IsUser(),commands=['menu'])
async def user_menu(message:Message):
    markup = ReplyKeyboardMarkup(selective=True,resize_keyboard=True)
    markup.add(catalog)
    markup.row(balance,cart)
    markup.add(delivery_status)

    await message.answer(text="Menu",reply_markup=markup)
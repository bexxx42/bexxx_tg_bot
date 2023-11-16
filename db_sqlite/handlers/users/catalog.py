from aiogram.types import Message ,CallbackQuery
from aiogram.types.chat import ChatActions
from keyboards.default.markups import catalog
from keyboards.inline.categories import categories_markup,category_cb
from keyboards.inline.product_from_catalog import product_markup,product_cb
from filters import IsUser
from loader import dp,db,bot



@dp.message_handler(IsUser(),text=catalog)
async def process_catalog(message:Message)
    await message.answer(text='Tanlang',reply_markup=categories_markup())

@dp.callback_query_handlers(IsUser(),category_cb.filter(action='view'))
async def category_callback_handler(query:CallbackQuery,callback_data:dict)
    products =db.select_products_in_categories(callback_data['id'])
    await query.answer('Hamma tovarlar')
    await show_products(query.answer,products)
@dp.callback_query_handlers(IsUser(),product_cb.filter(action='add'))
async def add_product_callback_handler(query:CallbackQuery,callback:dict):
    await query.answer('Mahsulot qowildi')
    await query.message.delete()

async def show_products(message,products):
    if len(products) == 0:
        await message.answer('hec narsa yoq')
    else:
        await bot.send_chat_action(message.chat.id,ChatActions.TYPING)

        for idx,title,body,img,price,_ in products:
            markup = product_markup(idx,price)
            text = f"<b>{title}</b>\n\n{body}"
            await message.answer_photo(photo=imag,
                                       caption=text,
                                       reply_markup=markup)
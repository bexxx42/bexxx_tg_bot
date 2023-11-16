from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    language = State()

    fullName_uz = State()
    email_uz = State()
    phoneNum_uz = State()

    fullName_ru = State()
    email_ru = State()
    phoneNum_ru = State()

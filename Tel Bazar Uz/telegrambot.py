import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from buttons import *
from states import *

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6158421027:AAEc0CKk-NntBAiB6SvLfrkWyCR4cvqYwqU"

bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
TelBazarUz = Dispatcher(bot, storage=storage)


@TelBazarUz.message_handler(commands=["start"], state="*")
async def CMD_Start(message: types.Message):
    print(*message, sep='\n')
    await message.answer(
        "🇺🇿Assalomu aleykum🤝\n<b>TelBazarUz</b> rasmiy Telegram-botimizga xush kelibsiz!\nIltimos, til tanlang.",
        reply_markup=Select_Language_Button, parse_mode="HTML")
    await Condition.Language.set()


@TelBazarUz.message_handler(commands=["language"], state="*")
async def CMD_Languages(message: types.Message, state: FSMContext):
    await message.answer("🇺🇿Iltimos, til tanlang.", reply_markup=Select_Language_Button)
    await Condition.Language.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["O'zbek🇺🇿"], state=Condition.Language)
async def Incorrect_Languages(message: types.Message):
    return await message.answer("🇺🇿Iltimos, til tanlang.")


@TelBazarUz.message_handler(text="O'zbek🇺🇿", state=Condition.Language)
async def Uz_Language_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Language'] = message.text
    await message.answer("📞Admin siz bilan bog'lanishi uchun telefon raqamingizni yuboring.",
                         reply_markup=Uz_Contact_Button)
    await Condition.Uz_Phone_Number.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["📞Telefon raqamni yuborish"],
                            state=Condition.Uz_Phone_Number)
async def Incorrect_Uz_Phone_Number(message: types.Message):
    return await message.answer(
        "🚫Noto'g'ri telefon raqam kiritdingiz. Telefon raqamingizni yuborish uchun \"📞Telefon raqamni yuborish\" tugmasini bosing.")


@TelBazarUz.message_handler(content_types=["contact"], state=Condition.Uz_Phone_Number)
async def Uz_Contact_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_Phone_Number'] = message.contact.phone_number
    await message.answer("Bosh menyuga xush kelibsiz!",
                         reply_markup=Uz_PhonePricing_AirpodsPricing_ChangeLanguage_Button, parse_mode="HTML")
    await Condition.Uz_PhonePricing_AirpodsPricing_ChangeLanugage.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["📱Telefon", "🎧Airpods"],
                            state=Condition.Uz_PhonePricing_AirpodsPricing_ChangeLanugage)
async def Incorrect_Uz_PhonePricing_AirpodsPricing_ChangeLanugage(message: types.Message):
    return await message.answer("— Telefoningizni narxlash uchun ya'ni narxini aniqlab olish uchun\n<b>\"📱Telefon»</b> tugmasini bosing.\"\n\
— Airpodsingizni narxlash uchun ya'ni narxini aniqlab olish uchun <b>\"🎧Airpods\"</b> tugmasini bosing.\n\
— Tilni o'zgartirish uchun \"🌍<b>Tilni o'zgartirish\"</b> tugmasini bosing.", parse_mode="HTML")


@TelBazarUz.message_handler(text="📱Telefon", state=Condition.Uz_PhonePricing_AirpodsPricing_ChangeLanugage)
async def Uz_Phone_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_PhonePricing_AirpodsPricing_ChangeLanugage'] = message.text
    await message.answer("🤳🏻Telefoningiz modelini tanlang.", reply_markup=Uz_Telephones_Button)
    await Condition.Uz_Phone_Models.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["iPhone", "◀️Orqaga"], state=Condition.Uz_Phone_Models)
async def Incorrect_Uz_Phone_Models(message: types.Message):
    return await message.answer("🤳🏻Telefoningiz modelini tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_Phone_Models)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("Bosh menyuga xush kelibsiz!",
                         reply_markup=Uz_PhonePricing_AirpodsPricing_ChangeLanguage_Button)
    await Condition.Uz_PhonePricing_AirpodsPricing_ChangeLanugage.set()


# iPhone
@TelBazarUz.message_handler(text="iPhone", state=Condition.Uz_Phone_Models)
async def Uz_Phone_Models_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_Phone_Models'] = message.text
    await message.answer("📲Telefoningiz seriyasini tanlang.", reply_markup=Uz_iPhone_Series_Button)
    await Condition.Uz_Phone_Series.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["iPhone SE 2016", "◀️Orqaga"],
                            state=Condition.Uz_Phone_Series)
async def Incorrect_Uz_Phone_Series(message: types.Message):
    return await message.answer("📲Telefoningiz seriyasini tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_Phone_Series)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🤳🏻Telefoningiz modelini tanlang.", reply_markup=Uz_Telephones_Button)
    await Condition.Uz_Phone_Models.set()


# iPhone_SE_2016
@TelBazarUz.message_handler(text="iPhone SE 2016", state=Condition.Uz_Phone_Series)
async def Uz_iPhone_SE_2016_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_Phone_Series'] = message.text
    await message.answer("🔋Telefoningizni sig'imini tanlang.", reply_markup=Uz_iPhone_SE_2016_Battery_Button)
    await Condition.Uz_iPhone_SE_2016_Battery.set()


@TelBazarUz.message_handler(
    lambda message: message.text not in ["100-90%", "90-80%", "80-70%", "70-60%", "60-10%", "◀️Orqaga"],
    state=Condition.Uz_iPhone_SE_2016_Battery)
async def Incorrect_Uz_Batteries(message: types.Message):
    return await message.answer("🔋Telefoningizni sig'imini tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🔋Telefoningizni sig'imini tanlang.", reply_markup=Uz_iPhone_Series_Button)
    await Condition.Uz_Phone_Series.set()


@TelBazarUz.message_handler(text="100-90%", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_iPhone_SE_2016_Battery_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Battery'] = message.text
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(text="90-80%", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_iPhone_SE_2016_Battery_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Battery'] = message.text
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?.", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(text="80-70%", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_iPhone_SE_2016_Battery_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Battery'] = message.text
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(text="70-60%", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_iPhone_SE_2016_Battery_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Battery'] = message.text
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(text="60-10%", state=Condition.Uz_iPhone_SE_2016_Battery)
async def Uz_iPhone_SE_2016_Battery_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Battery'] = message.text
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["Ha✅", "Yo'q🚫", "◀️Orqaga"],
                            state=Condition.Uz_iPhone_SE_2016_DocBox)
async def Incorrect_Uz_iPhone_SE_2016_Colors(message: types.Message):
    return await message.answer("🗂Telefoningizni korobka dokumenti bormi?")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_DocBox)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🗂Telefoningizni korobka dokumenti bormi?", reply_markup=Uz_iPhone_SE_2016_Battery_Button)
    await Condition.Uz_iPhone_SE_2016_Battery.set()


@TelBazarUz.message_handler(text="Ha✅", state=Condition.Uz_iPhone_SE_2016_DocBox)
async def Uz_iPhone_SE_2016_DocBox_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_DocBox'] = "Bor"
    await message.answer("🎨Telefoningiz rangini tanlang.", reply_markup=Uz_iPhone_SE_2016_Colors_Button)
    await Condition.Uz_iPhone_SE_2016_Colors.set()


@TelBazarUz.message_handler(text="Yo'q🚫", state=Condition.Uz_iPhone_SE_2016_DocBox)
async def Uz_iPhone_SE_2016_DocBox_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_DocBox'] = "Yo'q"
    await message.answer("🎨Telefoningiz rangini tanlang.", reply_markup=Uz_iPhone_SE_2016_Colors_Button)
    await Condition.Uz_iPhone_SE_2016_Colors.set()


@TelBazarUz.message_handler(
    lambda message: message.text not in ["Rose Gold", "Gold", "Silver", "Space Gray", "◀️Orqaga"],
    state=Condition.Uz_iPhone_SE_2016_Colors)
async def Incorrect_Uz_iPhone_SE_2016_Colors(message: types.Message):
    return await message.answer("🎨Telefoningiz rangini tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Colors)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🎨Telefoningiz rangini tanlang.", reply_markup=Uz_iPhone_SE_2016_DocBox_Button)
    await Condition.Uz_iPhone_SE_2016_DocBox.set()


@TelBazarUz.message_handler(text="Rose Gold", state=Condition.Uz_iPhone_SE_2016_Colors)
async def Uz_iPhone_SE_2016_Color_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Colors'] = message.text
    await message.answer("🧠Telefoningizni xotirasini tanlang.", reply_markup=Uz_iPhone_SE_2016_Storage_Button)
    await Condition.Uz_iPhone_SE_2016_Storage.set()


@TelBazarUz.message_handler(text="Gold", state=Condition.Uz_iPhone_SE_2016_Colors)
async def Uz_iPhone_SE_2016_Color_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Colors'] = message.text
    await message.answer("🧠Telefoningizni xotirasini tanlang.", reply_markup=Uz_iPhone_SE_2016_Storage_Button)
    await Condition.Uz_iPhone_SE_2016_Storage.set()


@TelBazarUz.message_handler(text="Silver", state=Condition.Uz_iPhone_SE_2016_Colors)
async def Uz_iPhone_SE_2016_Color_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Colors'] = message.text
    await message.answer("🧠Telefoningizni xotirasini tanlang.", reply_markup=Uz_iPhone_SE_2016_Storage_Button)
    await Condition.Uz_iPhone_SE_2016_Storage.set()


@TelBazarUz.message_handler(text="Space Gray", state=Condition.Uz_iPhone_SE_2016_Colors)
async def Uz_iPhone_SE_2016_Color_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Colors'] = message.text
    await message.answer("🧠Telefoningizni xotirasini tanlang.", reply_markup=Uz_iPhone_SE_2016_Storage_Button)
    await Condition.Uz_iPhone_SE_2016_Storage.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["16", "32", "64", "◀️Orqaga"],
                            state=Condition.Uz_iPhone_SE_2016_Storage)
async def Incorrect_Uz_iPhone_SE_2016_Storage(message: types.Message):
    return await message.answer("🧠Telefoningizni xotirasini tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Storage)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🧠Telefoningizni xotirasini tanlang.", reply_markup=Uz_iPhone_SE_2016_Colors_Button)
    await Condition.Uz_iPhone_SE_2016_Colors.set()


@TelBazarUz.message_handler(text="16", state=Condition.Uz_iPhone_SE_2016_Storage)
async def Uz_iPhone_SE_2016_Storage_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Storage'] = message.text
    await message.answer("🌍Telefoningiz ishlab chiqarilgan joyni tanlang.",
                         reply_markup=Uz_iPhone_SE_2016_Created_Place_Button)
    await Condition.Uz_iPhone_SE_2016_Created_Place.set()


@TelBazarUz.message_handler(text="32", state=Condition.Uz_iPhone_SE_2016_Storage)
async def Uz_iPhone_SE_2016_Storage_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Storage'] = message.text
    await message.answer("🌍Telefoningiz ishlab chiqarilgan joyni tanlang.",
                         reply_markup=Uz_iPhone_SE_2016_Created_Place_Button)
    await Condition.Uz_iPhone_SE_2016_Created_Place.set()


@TelBazarUz.message_handler(text="64", state=Condition.Uz_iPhone_SE_2016_Storage)
async def Uz_iPhone_SE_2016_Storage_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Storage'] = message.text
    await message.answer("🌍Telefoningiz ishlab chiqarilgan joyni tanlang.",
                         reply_markup=Uz_iPhone_SE_2016_Created_Place_Button)
    await Condition.Uz_iPhone_SE_2016_Created_Place.set()


@TelBazarUz.message_handler(
    lambda message: message.text not in ["USA|LL", "China|CH", "UAE|AB", "Korea|KH", "◀️Orqaga"],
    state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Incorrect_Uz_iPhone_SE_2016_Created_Place(message: types.Message):
    return await message.answer("🌍Telefoningiz ishlab chiqarilgan joyni tanlang.")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🌍Telefoningiz ishlab chiqarilgan joyni tanlang.",
                         reply_markup=Uz_iPhone_SE_2016_Storage_Button)
    await Condition.Uz_iPhone_SE_2016_Storage.set()


@TelBazarUz.message_handler(text="USA|LL", state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Uz_iPhone_SE_2016_Created_Place_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Created_Place'] = message.text
    await message.answer("🛡Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Injury_Button)
    await Condition.Uz_iPhone_SE_2016_Injury.set()


@TelBazarUz.message_handler(text="China|CH", state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Uz_iPhone_SE_2016_Created_Place_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Created_Place'] = message.text
    await message.answer("🛡Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Injury_Button)
    await Condition.Uz_iPhone_SE_2016_Injury.set()


@TelBazarUz.message_handler(text="UAE|AB", state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Uz_iPhone_SE_2016_Created_Place_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Created_Place'] = message.text
    await message.answer("🛡Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Injury_Button)
    await Condition.Uz_iPhone_SE_2016_Injury.set()


@TelBazarUz.message_handler(text="Korea|KH", state=Condition.Uz_iPhone_SE_2016_Created_Place)
async def Uz_iPhone_SE_2016_Created_Place_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Created_Place'] = message.text
    await message.answer("🛡Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Injury_Button)
    await Condition.Uz_iPhone_SE_2016_Injury.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["Ha✅", "Yo'q🚫", "◀️Orqaga"],
                            state=Condition.Uz_iPhone_SE_2016_Injury)
async def Incorrect_Uz_iPhone_SE_2016_Injury(message: types.Message):
    return await message.answer("🛡Telefoningiz zarar ko'rganmi?")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Injury)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("🛡Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Created_Place_Button)
    await Condition.Uz_iPhone_SE_2016_Created_Place.set()


@TelBazarUz.message_handler(text="Yo'q🚫", state=Condition.Uz_iPhone_SE_2016_Injury)
async def Uz_iPhone_SE_2016_Injury_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Injury'] = "Yo'q"
    await bot.send_message(
        1329197690,
        md.text(
            md.text("Telefon modeli:", md.text(data["Uz_Phone_Models"])),
            md.text("Telefon seriyasi:", md.text(data["Uz_Phone_Series"])),
            md.text("\n🔋Sig'imi:", md.text(data["Uz_iPhone_SE_2016_Battery"])),
            md.text("📦+📄:", md.text(data["Uz_iPhone_SE_2016_DocBox"])),
            md.text("🎨Rangi:", md.text(data["Uz_iPhone_SE_2016_Colors"])),
            md.text("🧠Xotirasi:", md.text(data["Uz_iPhone_SE_2016_Storage"])),
            md.text("🌍Ishlab chiqarilgan joy:", md.text(data["Uz_iPhone_SE_2016_Created_Place"])),
            md.text("🛡Zarar yetganmi?:", md.text(data["Uz_iPhone_SE_2016_Injury"])),
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()


@TelBazarUz.message_handler(text="Ha✅", state=Condition.Uz_iPhone_SE_2016_Injury)
async def Uz_iPhone_SE_2016_Injury_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Injury'] = "Ha"
    await message.answer(
        "Telefoningizni necha foizi zarar ko'rgan?\n\n30% (kamera xira, qirilgan va batareyka almashgan.)\n\n50% (ekran va kamera almashgan, barmoq izi va face id ishlamaydi.)",
        reply_markup=Uz_iPhone_SE_2016_Damage_Button)
    await Condition.Uz_iPhone_SE_2016_Damage.set()


@TelBazarUz.message_handler(lambda message: message.text not in ["30%", "50%", "◀️Orqaga"],
                            state=Condition.Uz_iPhone_SE_2016_Damage)
async def Incorrect_Uz_Phone_Models(message: types.Message):
    return await message.answer(
        "Telefoningizni necha foizi zarar ko'rgan?\n\n30% (kamera xira, qirilgan va batareyka almashgan.)\n\n50% (ekran va kamera almashgan, barmoq izi va face id ishlamaydi.)")


@TelBazarUz.message_handler(text="◀️Orqaga", state=Condition.Uz_iPhone_SE_2016_Damage)
async def Uz_Back_Process(message: types.Message, state: FSMContext):
    await message.answer("Telefoningiz zarar ko'rganmi?", reply_markup=Uz_iPhone_SE_2016_Injury_Button)
    await Condition.Uz_iPhone_SE_2016_Injury.set()


@TelBazarUz.message_handler(text="30%", state=Condition.Uz_iPhone_SE_2016_Damage)
async def Uz_iPhone_SE_2016_Damage_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Damage'] = message.text
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Telefon modeli:", md.text(data["Uz_Phone_Models"])),
            md.text("Telefon seriyasi:", md.text(data["Uz_Phone_Series"])),
            md.text("\n🔋Sig'imi:", md.text(data["Uz_iPhone_SE_2016_Battery"])),
            md.text("📦+📄:", md.text(data["Uz_iPhone_SE_2016_DocBox"])),
            md.text("🎨Rangi:", md.text(data["Uz_iPhone_SE_2016_Colors"])),
            md.text("🧠Xotirasi:", md.text(data["Uz_iPhone_SE_2016_Storage"])),
            md.text("🌍Ishlab chiqarilgan joy:", md.text(data["Uz_iPhone_SE_2016_Created_Place"])),
            md.text("🛡Zarar yetganmi?:", md.text(data["Uz_iPhone_SE_2016_Injury"])),
            md.text("🛠Necha foizi zarar ko'rgan?:", md.text(data["Uz_iPhone_SE_2016_Damage"])),
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()


@TelBazarUz.message_handler(text="50%", state=Condition.Uz_iPhone_SE_2016_Damage)
async def Uz_iPhone_SE_2016_Damage_Process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Uz_iPhone_SE_2016_Damage'] = message.text
        print(message.from_user.id)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Telefon modeli:", md.text(data["Uz_Phone_Models"])),
            md.text("Telefon seriyasi:", md.text(data["Uz_Phone_Series"])),
            md.text("\n🔋Sig'imi:", md.text(data["Uz_iPhone_SE_2016_Battery"])),
            md.text("📦+📄:", md.text(data["Uz_iPhone_SE_2016_DocBox"])),
            md.text("🎨Rangi:", md.text(data["Uz_iPhone_SE_2016_Colors"])),
            md.text("🧠Xotirasi:", md.text(data["Uz_iPhone_SE_2016_Storage"])),
            md.text("🌍Ishlab chiqarilgan joy:", md.text(data["Uz_iPhone_SE_2016_Created_Place"])),
            md.text("🛡Zarar yetganmi?:", md.text(data["Uz_iPhone_SE_2016_Injury"])),
            md.text("🛠Necha foizi zarar ko'rgan?:", md.text(data["Uz_iPhone_SE_2016_Damage"])),
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(TelBazarUz, skip_updates=True)

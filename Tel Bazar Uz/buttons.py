from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

Uz=KeyboardButton("O'zbek🇺🇿")
Select_Language_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz)

Uz_Phone_Number=KeyboardButton("📞Telefon raqamni yuborish", request_contact=True)
Uz_Contact_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_Phone_Number)

Uz_Phone_Pricing=KeyboardButton("📱Telefon")
Uz_Airpods=KeyboardButton("🎧Airpods")
Uz_PhonePricing_AirpodsPricing_ChangeLanguage_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_Phone_Pricing).add(Uz_Airpods)

Uz_iPhone=KeyboardButton("iPhone")
Uz_Back=KeyboardButton("◀️Orqaga")
Uz_Telephones_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone).add(Uz_Back)

Uz_iPhone_SE_2016=KeyboardButton("iPhone SE 2016")
Uz_iPhone_Series_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016).add(Uz_Back)

Uz_iPhone_SE_2016_Cool=KeyboardButton("100-90%")
Uz_iPhone_SE_2016_Great=KeyboardButton("90-80%")
Uz_iPhone_SE_2016_Normal=KeyboardButton("80-70%")
Uz_iPhone_SE_2016_Low=KeyboardButton("70-60%")
Uz_iPhone_SE_2016_Very_Low=KeyboardButton("60-10%")
Uz_iPhone_SE_2016_Battery_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016_Cool, Uz_iPhone_SE_2016_Great).add(Uz_iPhone_SE_2016_Normal, Uz_iPhone_SE_2016_Low).add(Uz_iPhone_SE_2016_Very_Low).add(Uz_Back)

Uz_iPhone_SE_2016_Rose_Gold=KeyboardButton("Rose Gold")
Uz_iPhone_SE_2016_Gold=KeyboardButton("Gold")
Uz_iPhone_SE_2016_Silver=KeyboardButton("Silver")
Uz_iPhone_SE_2016_Space_Gray=KeyboardButton("Space Gray")
Uz_iPhone_SE_2016_Colors_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016_Rose_Gold, Uz_iPhone_SE_2016_Gold).add(Uz_iPhone_SE_2016_Silver, Uz_iPhone_SE_2016_Space_Gray).add(Uz_Back)

Uz_Yes=KeyboardButton("Ha✅")
Uz_No=KeyboardButton("Yo'q🚫")
Uz_iPhone_SE_2016_DocBox_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_Yes, Uz_No).add(Uz_Back)

Uz_iPhone_SE_2016_16=KeyboardButton("16")
Uz_iPhone_SE_2016_32=KeyboardButton("32")
Uz_iPhone_SE_2016_64=KeyboardButton("64")
Uz_iPhone_SE_2016_Storage_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016_16, Uz_iPhone_SE_2016_32).add(Uz_iPhone_SE_2016_64).add(Uz_Back)

Uz_iPhone_SE_2016_USALL=KeyboardButton("USA|LL")
Uz_iPhone_SE_2016_ChinaCH=KeyboardButton("China|CH")
Uz_iPhone_SE_2016_UAEAB=KeyboardButton("UAE|AB")
Uz_iPhone_SE_2016_KoreaKH=KeyboardButton("Korea|KH")
Uz_iPhone_SE_2016_Created_Place_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016_USALL, Uz_iPhone_SE_2016_ChinaCH).add(Uz_iPhone_SE_2016_UAEAB, Uz_iPhone_SE_2016_KoreaKH).add(Uz_Back)

Uz_Yes=KeyboardButton("Ha✅")
Uz_No=KeyboardButton("Yo'q🚫")
Uz_iPhone_SE_2016_Injury_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_Yes, Uz_No).add(Uz_Back)

Uz_iPhone_SE_2016_Norm_Damage=KeyboardButton("30%")
Uz_iPhone_SE_2016_Big_Damage=KeyboardButton("50%")
Uz_iPhone_SE_2016_Damage_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(Uz_iPhone_SE_2016_Norm_Damage, Uz_iPhone_SE_2016_Big_Damage).add(Uz_Back)
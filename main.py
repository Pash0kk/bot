from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5813737364:AAHc26iZ6679vuoLh6i45RGJCWg8pKPFPQ4"

ABOUT_US = """
Наша компанія ТОВ "ВладоТурСервіс" займається організацією турів вже 12 років. Основний профіль нашої діяльності - гірськолижні тури по Україні та Європі.
Також з великим задоволенням ми організуємо для Вас корпоратив любої складності та чисельності. Ми прибічники активного туризму, тому походи та сплави - 
це також наше як в Україні так і за кордоном. А якщо Ви хочете купити тур з відпочинком на морі в Турції чи Єгипті чи ще деінде), або ж екскурсійний тур по Україні чи по Європі -
ми також допоможемо Вам в цьому). Завжди будемо Вам раді бачити Вас у нас в офісі, а також чути по телефону))
"""

bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot started')

def get_main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Про нас')
    b2 = KeyboardButton(text='Гірськолижні тури')
    b3 = KeyboardButton(text='Активний відпочинок')
    b4 = KeyboardButton(text='Екскурсійні тури')
    kb.add(b1).add(b2).add(b3).add(b4)

    return kb

def get_mountain_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Україна')
    b2 = KeyboardButton(text='Інші країни')
    kb.add(b1, b2)

    return kb

def get_ua_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton(text='БУКОВЕЛЬ 2 ДНІ КАТАННЯ', url='http://vladotour.com.ua/bukovel-2-dni-katannja-vijzd-po-pjatnicjah')
    ib2 = InlineKeyboardButton(text='БУКОВЕЛЬ 3 ДНІ КАТАННЯ', url='http://vladotour.com.ua/bukovel-3-dni-katannja-chernihiv')
    ib3 = InlineKeyboardButton(text='БУКОВЕЛЬ 3 ДНІ КАТАННЯ', url='http://vladotour.com.ua/bukovel-3-dni-katannja-vijzd-po-chetvergam')
    ib4 = InlineKeyboardButton(text='БУКОВЕЛЬ 4 ДНІ КАТАННЯ', url='http://vladotour.com.ua/bukovel-budni-dni-chotiri-dni-katannja-vijzd-kozhnoj-nedili')
    ib5 = InlineKeyboardButton(text='БУКОВЕЛЬ 7 ДНІ КАТАННЯ', url='http://vladotour.com.ua/bukovel-nedilja-na-kurorti-7-dniv-katannja')
    ikb.add(ib1, ib2).add(ib3, ib4).add(ib5)

    return ikb

def get_other_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton(text='АВТОБУСНІ ТУРИ', url='http://vladotour.com.ua/avtobusni-turi-z-mozhlivistju-priednatisja-v-evropi')
    ib2 = InlineKeyboardButton(text='ІТАЛІЯ - LIVIGNO. ВІДКРИТТЯ ЗИМОВОГО СЕЗОНУ', url='http://vladotour.com.ua/vidkrittja-sezonu-2019-2020-livigno-italy-ski-pass-bezkoshtovno')
    ib3 = InlineKeyboardButton(text='ФРАНЦІЯ - РІЗДВО НА КУРОРТІ', url='http://vladotour.com.ua/rizdvo-v-troh-dolinah-francija-meribel-kurshavel-val-torans')
    ib4 = InlineKeyboardButton(text='АВСТРІЯ -5 РЕГІОНІВ', url='http://vladotour.com.ua/esr-evropa-sport-region-avstrija-ski-safari-tur')
    ib5 = InlineKeyboardButton(text='ІТАЛІЯ - LIVIGNO. ЗАКРИТТЯ ЗИМОВОГО СЕЗОНУ', url='http://vladotour.com.ua/livigno-vesna-2022-zakrittja-sezonu')
    ikb.add(ib1, ib2).add(ib3, ib4).add(ib5)

    return ikb

def get_active_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='ОЗЕРО В БОБРИЦЮ', url='http://vladotour.com.ua/sup---tur-na-korostishivskii-kar-er-1-den')
    ib2 = InlineKeyboardButton(text='КИЇВСЬКЕ МОРЕ', url='http://vladotour.com.ua/sup--tur-na-kijvske-more-1-den-')
    ib3 = InlineKeyboardButton(text='КАРПАТИ', url='http://vladotour.com.ua/aktiv-tur-v-karpati-veloproguljanka-rafting--pohid-na-goverlu')
    ib4 = InlineKeyboardButton(text='ПРОКАТ SUP БОРДІВ В КИЄВІ', url='http://vladotour.com.ua/prokat-sup-bordiv-v-kievi')
    ikb.add(ib1, ib2).add(ib3, ib4)

    return ikb

def get_trip_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton(text='ЕКСКУРСІЯ В ЧОРНОБИЛЬ', url='http://vladotour.com.ua/ekskursija-v-chornobil-i-pripjat-na-dva-dni')
    ib2 = InlineKeyboardButton(text="КОРОЛІВСЬКИЙ КАМ'ЯНЕЦЬ", url='http://vladotour.com.ua/korolivskii-kamjanec')
    ib3 = InlineKeyboardButton(text='СПАДЩИНА ТРИПІЛЬЦІВ', url='http://vladotour.com.ua/miscjami-kulturnoj-spadshhini-tripilciv---odnodennii-tur')
    ib4 = InlineKeyboardButton(text='ТУР ДО ЧОРНОБИЛЬСЬКОЇ ЗОНИ ВІДЧУЖЕННЯ', url='http://vladotour.com.ua/odnodennii-tur-do-chornobilskoj-zoni-vidchuzhennja')
    ib5 = InlineKeyboardButton(text='ПОЛТАВСЬКІ ВИТРЕБЕНЬКИ', url='http://vladotour.com.ua/poltavski-vitrebenki')
    ib6 = InlineKeyboardButton(text='ТАМ, ДЕ ГОРИ Й ПОЛОНИНИ', url='http://vladotour.com.ua/tam-de-gori-i-polonini-%7C-tur-v-karpati-na-vihidni')
    ikb.add(ib1, ib2).add(ib3, ib4).add(ib5, ib6)

    return ikb

def get_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='У меню'))

    return kb




@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.answer("Доброго дня, раді вітати Вас на нашому боті!", reply_markup=get_main_keyboard())

@dp.message_handler(Text(equals='У меню'))
async def cancel_btn(message: types.Message):
    await message.answer("Ви повернулися у меню!", reply_markup=get_main_keyboard())

@dp.message_handler(Text(equals='Про нас'))
async def about_btn(message: types.Message):
    await message.answer(ABOUT_US, reply_markup=get_cancel())

@dp.message_handler(Text(equals='Гірськолижні тури'))
async def moun_btn(message: types.Message):
    await message.answer("Оберіть країну", reply_markup=get_mountain_keyboard())

@dp.message_handler(Text(equals='Україна'))
async def ua_btn(message: types.Message):
    await message.answer("Оберіть один із представлених турів", reply_markup=get_ua_keyboard())
    await message.answer("Натисність кнопку 'у меню', щоб повернутись у головне меню", reply_markup=get_cancel())

@dp.message_handler(Text(equals='Інші країни'))
async def other_btn(message: types.Message):
    await message.answer("Оберіть один із представлених турів", reply_markup=get_other_keyboard())
    await message.answer("Натисність кнопку 'у меню', щоб повернутись у головне меню", reply_markup=get_cancel())



@dp.message_handler(Text(equals='Активний відпочинок'))
async def active_btn(message: types.Message):
    await message.answer("Оберіть один із представлених варіантів", reply_markup=get_active_keyboard())
    await message.answer("Натисність кнопку 'у меню', щоб повернутись у головне меню", reply_markup=get_cancel())



@dp.message_handler(Text(equals='Екскурсійні тури'))
async def active_btn(message: types.Message):
    await message.answer("Оберіть один із представлених варіантів", reply_markup=get_trip_keyboard())
    await message.answer("Натисність кнопку 'у меню', щоб повернутись у головне меню", reply_markup=get_cancel())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

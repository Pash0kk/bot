from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3 as sq


TOKEN = "5813737364:AAHc26iZ6679vuoLh6i45RGJCWg8pKPFPQ4"

ABOUT_US = """
Наша компанія ТОВ "ВладоТурСервіс" займається організацією турів вже 12 років. Основний профіль нашої діяльності - гірськолижні тури по Україні та Європі.
Також з великим задоволенням ми організуємо для Вас корпоратив любої складності та чисельності. Ми прибічники активного туризму, тому походи та сплави - 
це також наше як в Україні так і за кордоном. А якщо Ви хочете купити тур з відпочинком на морі в Турції чи Єгипті чи ще деінде), або ж екскурсійний тур по Україні чи по Європі -
ми також допоможемо Вам в цьому). Завжди будемо Вам раді бачити Вас у нас в офісі, а також чути по телефону))
"""

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_):
    await db_start()
    print('Bot started')

async def db_start():
    global db, cur

    db = sq.connect('managers.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS clients(user_id TEXT PRIMARY KEY, type TEXT, name TEXT, date TEXT, place TEXT, category TEXT, count TEXT, insurance TEXT, equipment TEXT, skips TEXT)")

    db.commit()

async def create_profile(user_id, name):
    
    user = cur.execute("SELECT 1 FROM clients WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO clients VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, '', name, '', '', '', '', '', '', ''))
        db.commit()

async def edit_profile(state, user_id, name):
    async with state.proxy() as data:
        cur.execute("UPDATE clients SET type = '{}', name = '{}', date = '{}', place = '{}', category = '{}', count = '{}', insurance = '{}', equipment = '{}', skips = '{}' WHERE user_id == '{}'".format(data['type'], name, data['date'], data['place'], data['category'], data['count'], data['insurance'], data['equipment'], data['skips'], user_id))
        db.commit()

async def get_data(message):
    for i in cur.execute("SELECT * FROM clients").fetchall():
        await bot.send_message(message.from_user.id, f"Є замовлення від @{i[2]}. \nТип поїздки: {i[1]} \nДата виїзду: {i[3]} \nМісто виїзду: {i[4]} \nКатегорія проживання: {i[5]} \nКількість чоловік: {i[6]} \nСтрахування: {i[7]} \nСпорядження: {i[8]} \nСкіпаси: {i[9]}")



class ClientStateGroup(StatesGroup):

    main_state = State()
    tour_state = State()

    date_state = State()
    place_state = State()
    category_state = State()
    count_state = State()
    insurance_state = State()
    equip_state = State()
    skips_state = State()

    manage_state = State()


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
    b3 = KeyboardButton(text='У меню')
    kb.add(b1, b2).add(b3)

    return kb

def get_ua_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='БУКОВЕЛЬ 2 ДНІ КАТАННЯ')
    b2 = KeyboardButton(text='БУКОВЕЛЬ 3 ДНІ КАТАННЯ')
    b3 = KeyboardButton(text='БУКОВЕЛЬ 3 ДНІ КАТАННЯ')
    b4 = KeyboardButton(text='БУКОВЕЛЬ 4 ДНІ КАТАННЯ')
    b5 = KeyboardButton(text='БУКОВЕЛЬ 7 ДНІ КАТАННЯ')
    b6 = KeyboardButton(text='У меню')
    kb.add(b1, b2).add(b3, b4).add(b5).add(b6)

    return kb

def get_place_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Київ')
    b2 = KeyboardButton(text='Чернігів')
    b3 = KeyboardButton(text='Відмінити')
    kb.add(b1, b2).add(b3)

    return kb

def get_category_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Котедж')
    b2 = KeyboardButton(text='Готель')
    b3 = KeyboardButton(text='Відмінити')
    kb.add(b1, b2).add(b3)

    return kb

def get_variant_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='Так')
    b2 = KeyboardButton(text='Ні')
    b3 = KeyboardButton(text='Відмінити')
    kb.add(b1, b2).add(b3)

    return kb


def get_manager_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='Замовлення'))

    return kb


def get_other_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='АВТОБУСНІ ТУРИ')
    b2 = KeyboardButton(text='ІТАЛІЯ - LIVIGNO. ВІДКРИТТЯ ЗИМОВОГО СЕЗОНУ')
    b3 = KeyboardButton(text='ФРАНЦІЯ - РІЗДВО НА КУРОРТІ')
    b4 = KeyboardButton(text='АВСТРІЯ -5 РЕГІОНІВ')
    b5 = KeyboardButton(text='ІТАЛІЯ - LIVIGNO. ЗАКРИТТЯ ЗИМОВОГО СЕЗОНУ')
    b6 = KeyboardButton(text='У меню')
    kb.add(b1, b2).add(b3, b4).add(b5).add(b6)

    return kb

def get_active_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='ОЗЕРО В БОБРИЦЮ')
    b2 = KeyboardButton(text='КИЇВСЬКЕ МОРЕ')
    b3 = KeyboardButton(text='КАРПАТИ')
    b4 = KeyboardButton(text='ПРОКАТ SUP БОРДІВ В КИЄВІ')
    b5 = KeyboardButton(text='У меню')
    kb.add(b1, b2).add(b3, b4).add(b5)

    return kb

def get_trip_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='ЕКСКУРСІЯ В ЧОРНОБИЛЬ')
    b2 = KeyboardButton(text="КОРОЛІВСЬКИЙ КАМ'ЯНЕЦЬ")
    b3 = KeyboardButton(text='СПАДЩИНА ТРИПІЛЬЦІВ')
    b4 = KeyboardButton(text='ТУР ДО ЧОРНОБИЛЬСЬКОЇ ЗОНИ ВІДЧУЖЕННЯ')
    b5 = KeyboardButton(text='ПОЛТАВСЬКІ ВИТРЕБЕНЬКИ')
    b6 = KeyboardButton(text='ТАМ, ДЕ ГОРИ Й ПОЛОНИНИ')
    b7 = KeyboardButton(text='У меню')
    kb.add(b1, b2).add(b3, b4).add(b5, b6).add(b7)

    return kb

def get_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='У меню'))

    return kb




@dp.message_handler(commands = ['start'], state=None)
async def start_command(message: types.Message):
    
    admin = cur.execute("SELECT user_id FROM users WHERE user_id == '{key}'".format(key=message.from_user.id)).fetchone()
    if not admin:
        await ClientStateGroup.main_state.set()
        await message.answer("Доброго дня, раді вітати Вас на нашому боті!", reply_markup=get_main_keyboard())
        await create_profile(user_id=message.from_user.id, name=message.from_user.username)
    else:
        await message.answer(f"Доброго дня, менеджер {message.from_user.full_name}!", reply_markup=get_manager_keyboard())
        await ClientStateGroup.manage_state.set()




@dp.message_handler(Text(equals=['У меню', 'Відмінити']), state="*")
async def cancel_btn(message: types.Message, state: FSMContext):
    if state is None:
        return
    
    await state.finish()
    await message.answer("Ви повернулися у меню!", reply_markup=get_main_keyboard())



@dp.message_handler(Text(equals='Про нас'), state=ClientStateGroup.main_state)
async def about_btn(message: types.Message):
    await message.answer(ABOUT_US, reply_markup=get_cancel())

@dp.message_handler(Text(equals='Гірськолижні тури'), state=ClientStateGroup.main_state)
async def moun_btn(message: types.Message):
    await message.answer("Оберіть країну", reply_markup=get_mountain_keyboard())

@dp.message_handler(Text(equals='Україна'), state=ClientStateGroup.main_state)
async def ua_btn(message: types.Message):
    await message.answer("Оберіть один із представлених турів", reply_markup=get_ua_keyboard())
    await ClientStateGroup.tour_state.set()

@dp.message_handler(Text(equals='Інші країни'), state=ClientStateGroup.main_state)
async def other_btn(message: types.Message):
    await message.answer("Оберіть один із представлених турів", reply_markup=get_other_keyboard())
    await ClientStateGroup.tour_state.set()

@dp.message_handler(Text(equals='Активний відпочинок'), state=ClientStateGroup.main_state)
async def active_btn(message: types.Message):
    await message.answer("Оберіть один із представлених варіантів", reply_markup=get_active_keyboard())
    await ClientStateGroup.tour_state.set()

@dp.message_handler(Text(equals='Екскурсійні тури'), state=ClientStateGroup.main_state)
async def active_btn(message: types.Message):
    await message.answer("Оберіть один із представлених варіантів", reply_markup=get_trip_keyboard())
    await ClientStateGroup.tour_state.set()



@dp.message_handler(state=ClientStateGroup.tour_state)
async def check_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
    
    await message.answer("Оберіть дату виїзду", reply_markup=ReplyKeyboardRemove(True))
    await ClientStateGroup.date_state.set()


@dp.message_handler(state=ClientStateGroup.date_state)
async def check_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("Дату прийнято. \nОберіть місто з виїзду", reply_markup=get_place_keyboard())
    await ClientStateGroup.next()

@dp.message_handler(Text(equals=['Київ', 'Чернігів']), state=ClientStateGroup.place_state)
async def check_place(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place'] = message.text
    await message.answer("Місто прийнято. \nОберіть категорію проживання", reply_markup=get_category_keyboard())
    await ClientStateGroup.next()

@dp.message_handler(Text(equals=['Котедж', 'Готель']), state=ClientStateGroup.category_state)
async def check_cat(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer("Категорію проживання прийнято. \nЯка кількість чоловік?", reply_markup=ReplyKeyboardRemove(True))
    await ClientStateGroup.next()

# проверка на числа

@dp.message_handler(lambda message: not message.text.isdigit(), state=ClientStateGroup.count_state)
async def check_count(message: types.Message, state: FSMContext):
    await message.answer("Ви ввели не число!")

@dp.message_handler(state=ClientStateGroup.count_state)
async def load_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['count'] = message.text
    await message.answer("Кількість прийнято. \nЧи потрібно вам страхування?", reply_markup=get_variant_keyboard())
    await ClientStateGroup.next()

@dp.message_handler(Text(equals=['Так', 'Ні']), state=ClientStateGroup.insurance_state)
async def check_insurance(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['insurance'] = message.text
    await message.answer("Чи потрібно вам спорядження?", reply_markup=get_variant_keyboard())
    await ClientStateGroup.next()

@dp.message_handler(Text(equals=['Так', 'Ні']), state=ClientStateGroup.equip_state)
async def check_equip(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['equipment'] = message.text
    await message.answer("Чи потрібні вам скіпаси?", reply_markup=get_variant_keyboard())
    await ClientStateGroup.next()

@dp.message_handler(Text(equals=['Так', 'Ні']), state=ClientStateGroup.skips_state)
async def check_skips(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['skips'] = message.text

    await message.answer("Дякуємо, менеджер напрямку з вами звяжеться протягом 5 хвилин.", reply_markup=get_cancel())
    await edit_profile(state, message.from_user.id, message.from_user.username)
    await state.finish()




@dp.message_handler(Text(equals='Замовлення'), state=ClientStateGroup.manage_state)
async def check_manager(message: types.Message):
    await get_data(message)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

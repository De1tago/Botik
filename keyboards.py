from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Главное меню с инлайн-кнопками
def get_main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text='🌤 Погода сейчас', callback_data='weather_now')],
        [InlineKeyboardButton(text='🕒 По времени суток', callback_data='weather_dayparts')],
        [InlineKeyboardButton(text='📅 Прогноз на 3 дня', callback_data='weather_dayparts3')],
        [InlineKeyboardButton(text='🌍 Погода по геолокации', callback_data='weather_geo')],
        [
            InlineKeyboardButton(text='⭐️ Мои города', callback_data='fav_cities'),
            InlineKeyboardButton(text='➕ Добавить город', callback_data='fav_add'),
            InlineKeyboardButton(text='➖ Удалить город', callback_data='fav_del'),
        ],
        [InlineKeyboardButton(text='🕓 История запросов', callback_data='history')],
        [InlineKeyboardButton(text='ℹ️ Помощь', callback_data='help')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Клавиатура для запроса геолокации
geo_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отправить геолокацию', request_location=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards import get_main_menu

router = Router()

@router.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я бот, который может показать погоду.\n\n"
        "Выберите действие с помощью кнопок ниже или используйте команды.\n\n"
        "Доступные команды:\n"
        "/weather <город> — текущая погода.\n"
        "/dayparts <город> — погода по времени суток (ночь, утро, день, вечер) на сегодня.\n"
        "/dayparts3 <город> — погода по времени суток на ближайшие 3 дня.\n"
        "/geo — погода по вашей геолокации.\n"
        "/addcity <город> — добавить город в избранные.\n"
        "/delcity <город> — удалить город из избранных.\n"
        "/mycities — показать ваши избранные города.\n"
        "/history — история ваших последних запросов.\n\n"
        "Примеры:\n"
        "/weather Москва\n"
        "/dayparts Саратов\n"
        "/dayparts3 Санкт-Петербург\n"
        "/geo\n"
        "/addcity Казань\n"
        "/delcity Казань\n"
        "/mycities\n"
        "/history"
        ,
        reply_markup=get_main_menu()
    )

@router.callback_query(lambda c: c.data in [
    'weather_now', 'weather_dayparts', 'weather_dayparts3', 'weather_geo',
    'fav_cities', 'fav_add', 'fav_del', 'history', 'help'])
async def main_menu_callback(callback: CallbackQuery):
    if callback.data == 'weather_now':
        await callback.message.answer('Введите команду /weather <город> или напишите город в ответ на это сообщение.')
    elif callback.data == 'weather_dayparts':
        await callback.message.answer('Введите команду /dayparts <город> или напишите город в ответ на это сообщение.')
    elif callback.data == 'weather_dayparts3':
        await callback.message.answer('Введите команду /dayparts3 <город> или напишите город в ответ на это сообщение.')
    elif callback.data == 'weather_geo':
        await callback.message.answer('Для получения погоды по вашей геолокации используйте команду /geo или нажмите кнопку ниже.')
    elif callback.data == 'fav_cities':
        await callback.message.answer('Ваши избранные города можно посмотреть с помощью /mycities.')
    elif callback.data == 'fav_add':
        await callback.message.answer('Чтобы добавить город в избранные, используйте команду /addcity <город>.')
    elif callback.data == 'fav_del':
        await callback.message.answer('Чтобы удалить город из избранных, используйте команду /delcity <город>.')
    elif callback.data == 'history':
        await callback.message.answer('Историю последних запросов можно посмотреть с помощью /history.')
    elif callback.data == 'help':
        await callback.message.answer('Я могу показать погоду по вашему запросу. Используйте кнопки меню или команды из /start.')
    await callback.answer()

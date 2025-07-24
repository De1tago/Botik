from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from user_data import add_fav_city, remove_fav_city, get_fav_cities

router = Router()

@router.message(Command('addcity'))
async def add_city(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer('Пожалуйста, укажите город. Например: /addcity Москва')
        return
    city = args[1].strip()
    add_fav_city(message.from_user.id, city)
    await message.answer(f'Город {city} добавлен в избранные!')

@router.message(Command('delcity'))
async def del_city(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer('Пожалуйста, укажите город. Например: /delcity Москва')
        return
    city = args[1].strip()
    favs = get_fav_cities(message.from_user.id)
    if city in favs:
        remove_fav_city(message.from_user.id, city)
        await message.answer(f'Город {city} удалён из избранных.')
    else:
        await message.answer(f'Город {city} не найден в ваших избранных.')

@router.message(Command('mycities'))
async def my_cities(message: Message):
    favs = get_fav_cities(message.from_user.id)
    if not favs:
        await message.answer('У вас нет избранных городов. Добавьте их с помощью /addcity <город>.')
    else:
        await message.answer('Ваши избранные города:\n' + '\n'.join(favs), parse_mode='HTML')

@router.callback_query(lambda c: c.data == 'fav_cities')
async def fav_cities_callback(callback: CallbackQuery):
    favs = get_fav_cities(callback.from_user.id)
    if not favs:
        await callback.message.answer('У вас нет избранных городов. Добавьте их с помощью /addcity <город>.')
    else:
        await callback.message.answer('Ваши избранные города:\n' + '\n'.join(favs), parse_mode='HTML')
    await callback.answer()

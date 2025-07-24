from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from weather_api import get_weather, get_day_parts_weather, get_day_parts_weather_3days
from user_data import add_to_history

router = Router()

@router.message(Command('weather'))
async def weather_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите город. Например: /weather Москва")
        return
    city = args[1].strip()
    add_to_history(message.from_user.id, city)
    weather_info = await get_weather(city)
    await message.answer(weather_info, parse_mode='HTML')

@router.message(Command('dayparts'))
async def dayparts_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите город. Например: /dayparts Москва")
        return
    city = args[1].strip()
    add_to_history(message.from_user.id, city)
    weather_info = await get_day_parts_weather(city)
    await message.answer(weather_info, parse_mode='HTML')

@router.message(Command('dayparts3'))
async def dayparts3_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите город. Например: /dayparts3 Москва")
        return
    city = args[1].strip()
    add_to_history(message.from_user.id, city)
    weather_info = await get_day_parts_weather_3days(city)
    await message.answer(weather_info, parse_mode='HTML')

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import ClientSession
from keyboards import geo_keyboard
from weather_api import get_weather

router = Router()

@router.message(Command('geo'))
async def geo_request(message: Message):
    """
    Отправляет клавиатуру для запроса геолокации пользователя.
    """
    await message.answer('Пожалуйста, отправьте свою геолокацию с помощью кнопки ниже:', reply_markup=geo_keyboard)

@router.message(lambda m: m.location is not None)
async def handle_location(message: Message):
    """
    Обрабатывает сообщение с геолокацией, определяет город и показывает погоду.
    """
    lat = message.location.latitude
    lon = message.location.longitude
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=ru'
    async with ClientSession() as session:
        try:
            async with session.get(url, headers={'User-Agent': 'TelegramWeatherBot/1.0'}) as resp:
                data = await resp.json()
                city = data.get('address', {}).get('city') or \
                       data.get('address', {}).get('town') or \
                       data.get('address', {}).get('village') or \
                       data.get('address', {}).get('hamlet')
                if not city:
                    await message.answer('Не удалось определить город по координатам.')
                    return
                weather_info = await get_weather(city)
                await message.answer(f'Погода для вашего местоположения ({city}):\n{weather_info}', parse_mode='HTML')
        except Exception as e:
            await message.answer(f'Ошибка при определении города: {e}')

import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('Не найден BOT_TOKEN в .env')

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Импорт и регистрация роутеров
from handlers.weather import router as weather_router
from handlers.geo import router as geo_router
from handlers.fav_cities import router as fav_cities_router
from handlers.history import router as history_router
from handlers.menu import router as menu_router
from handlers.help import router as help_router

dp.include_router(menu_router)
dp.include_router(weather_router)
dp.include_router(geo_router)
dp.include_router(fav_cities_router)
dp.include_router(history_router)
dp.include_router(help_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 
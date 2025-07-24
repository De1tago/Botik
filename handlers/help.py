from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(
        'Я могу показать погоду по вашему запросу.\n'
        'Используйте кнопки меню или команды из /start.\n'
        'Если возникнут вопросы — просто напишите мне!'
    )

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from user_data import get_history

router = Router()

@router.message(Command('history'))
async def history_handler(message: Message):
    history = get_history(message.from_user.id)
    if not history:
        await message.answer('У вас пока нет истории запросов.')
    else:
        await message.answer('Последние города, по которым вы запрашивали погоду:\n' + '\n'.join(history), parse_mode='HTML')

@router.callback_query(lambda c: c.data == 'history')
async def history_callback(callback: CallbackQuery):
    history = get_history(callback.from_user.id)
    if not history:
        await callback.message.answer('У вас пока нет истории запросов.')
    else:
        await callback.message.answer('Последние города, по которым вы запрашивали погоду:\n' + '\n'.join(history), parse_mode='HTML')
    await callback.answer()

from aiogram import Router
from aiogram.types import Message


router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Я отвечаю твоим же сообщением\n'
                         f'на все что не прописано командах,\n'
                         f'посмотреть ты можешь нажав кнопку /help\n'
                         f'{message.text}', parse_mode='HTML')

from aiogram import types, F, Router  # Импортируем необходимые модули из библиотеки aiogram
from aiogram.types import Message  # Импортируем класс Message для работы с сообщениями
from aiogram.types.input_file import FSInputFile  # Импортируем FSInputFile для отправки файлов
from aiogram.filters import Command  # Импортируем фильтр Command для обработки команд

router = Router()  # Создаем экземпляр маршрутизатора (Router)

# Обработчик команды "/start"
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Лол кек❤️")  # Отправляем сообщение в ответ на команду "/start"

# Обработчик команды "/next"
@router.message(Command("next"))
async def start_handler(msg: Message):
    await msg.answer("некст")  # Отправляем сообщение в ответ на команду "/next"

# Обработчик команды "/photo"
@router.message(Command("photo"))
async def start_handler(msg: Message):
    photo_path = r'C:\Users\Администратор\Desktop\TelegramBot\Assets\TlNVhcx91xg.jpg'  # Путь к фото

    try:
        # Создаем объект FSInputFile для отправки фото
        photo = FSInputFile(photo_path)
        await msg.answer_photo(photo=photo, caption="Donald moment")  # Отправляем фото с подписью
    except Exception as e:
        await msg.answer(f"Ошибка: {e}")  # Отправляем сообщение об ошибке, если что-то пошло не так

# Обработчик всех остальных сообщений
@router.message()
async def message_handler(msg: Message):
    #await msg.answer(f"Твой ID: {msg.from_user.id}")  # (Закомментировано) Отправка ID пользователя
    await msg.answer("Чебурек❤️")  # Отправляем сообщение по умолчанию для всех остальных сообщений

import asyncio  # Импортируем модуль asyncio для работы с асинхронными функциями
import logging  # Импортируем модуль logging для логирования

from aiogram import Bot, Dispatcher  # Импортируем Bot и Dispatcher из aiogram для работы с ботом и диспетчером событий
from aiogram.enums.parse_mode import ParseMode  # Импортируем режим парсинга ParseMode для обработки форматирования сообщений
from aiogram.fsm.storage.memory import MemoryStorage  # Импортируем MemoryStorage для хранения состояний finite state machine (FSM) в памяти

import config  # Импортируем файл config, где хранится конфигурация, включая токен бота
from handlers import router  # Импортируем маршрутизатор для обработки команд и сообщений

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)  # Создаем объект бота с токеном и режимом парсинга HTML
    dp = Dispatcher(storage=MemoryStorage())  # Создаем объект диспетчера с хранилищем состояний в памяти
    dp.include_router(router)  # Подключаем маршрутизатор для обработки сообщений
    await bot.delete_webhook(drop_pending_updates=True)  # Удаляем вебхук и сбрасываем все незавершенные обновления
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())  # Запускаем процесс поллинга для приема обновлений от Telegram

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Настраиваем логирование на уровне INFO
    asyncio.run(main())  # Запускаем основную асинхронную функцию через asyncio

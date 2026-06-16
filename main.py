from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from database import init_db

TOKEN = "8332729649:AAF5cYtQIc1V5RjLnQg5TyZKrv_Z9GDsl_g"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем меню
def get_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Записаться на сессию", callback_data="book_session")],
        [InlineKeyboardButton(text="Мои записи", callback_data="my_appointments")]
    ])
    return keyboard

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Здравствуйте! Я ваш помощник. Выберите действие:",
        reply_markup=get_main_menu()
    )

# Обработка нажатия на кнопку "Записаться"
@dp.callback_query(F.data == "book_session")
async def book_session(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите удобное время:")
    await callback.answer()

async def main():
    await init_db()
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

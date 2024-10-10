import asyncio
import logging
import sys
from os import getenv
from os.path import exists

from aiogram.methods.send_photo import SendPhoto
from aiogram import Bot, Dispatcher, html, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup

import keyboards as kb


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8104928098:AAHojIyyVHwJj_3LtLKQbwn-FGxwnmq1wwU"
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
buttons = {
    'матешка': 'Матешка',
    'английский': 'Английский',
    'укрмова': 'Укр Мова',
}

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer("Привіт, readeHomeWork - це сервіс, в якому зроблять твій шкільний-університетський проєкт, домашку за невеликі гроші. У цьому боті ти можеш зареєструватися як той хто буде робити ДЗ", reply_markup=kb.regButton)



@dp.message(F.text == "Maksim")
async def say_that_maksim_is_gay(message: Message) -> None:
    await message.answer("Maksim is GAAAAY", reply_markup=kb.main)


@dp.message(F.text == "Зарегеструватися")
async def regStep1(message: Message) -> None:
    await message.answer("Будь ласка, обери предмети-напрямки в яких ти добре розбираєшся", reply_markup=kb.lessons)

lessons = {
    'матешка': "Матешка",
    'английский': "Английский",
    'укрмова': "УкрМова",
}


@dp.message(F.text == "Gay")
async def say_that_maksim_is_gay(message: Message) -> None:
    await message.answer_photo("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Atlas_deck_ace_of_hearts.svg/1200px-Atlas_deck_ace_of_hearts.svg.png", reply_markup=kb.testPay)

@dp.callback_query(lambda call: True)
async def callback_handler(call: types.CallbackQuery):
    buttons_text = []
    call_data = call.data.split('_')[1]
    if lessons[call_data][0] ==  '✅':
        lessons[call_data] = lessons[call_data][1:]
    else:
        lessons[call_data] = '✅' + lessons[call_data]



    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=lessons['матешка'], callback_data='lesson_матешка')],
        [InlineKeyboardButton(text=lessons['английский'], callback_data='lesson_английский')],
        [InlineKeyboardButton(text=lessons['укрмова'], callback_data='lesson_укрмова')]
    ])

    await call.message.edit_reply_markup(reply_markup=kb)




async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
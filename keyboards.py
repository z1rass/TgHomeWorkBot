from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

regButton = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Зарегеструватися')]
])

sendButton = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Надислати")]
])




lessons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Матешка", callback_data="select_матешка")],
    [InlineKeyboardButton(text="Английский", callback_data="select_английский")],
    [InlineKeyboardButton(text="УкрМова", callback_data="select_укрмова")]
])

mainKeyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Maksim")],
        [KeyboardButton(text="Gay")]
    ]
)

testPay = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Maksim", callback_data="Maksim")],
])

thms = [1, 2, 3, 4]


async def inline_cars():
    keyboard = ReplyKeyboardBuilder()
    for thm in thms:
        keyboard.add(KeyboardButton(text=thm))
    return keyboard.adjust(2).as_markup()

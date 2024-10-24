from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

'''
1. При регистрации бот предлагает пользователю выбрать свой знак зодиака. Используется ReplyKeyboardMarkup 3 ряда по 4 кнопки 
с эмоджи знака зодиака. После выбора знака бот присылает сообщение с информацией о выбранном знаке.
'''
'''♈️ ♉️ ♊️ ♋️ ♌️ ♓️ ♒️ ♑️ ♐️ ♏️ ♎️ ♍️'''

menu = [
    [
        InlineKeyboardButton(text="♈️", callback_data="Aries"),
        InlineKeyboardButton(text="♉️", callback_data="Taurus"),
        InlineKeyboardButton(text="♊️", callback_data="Gemini"),
        InlineKeyboardButton(text="♋️", callback_data="Cancer")
    ],
    [
        InlineKeyboardButton(text="♌️", callback_data="Leo"),
        InlineKeyboardButton(text="♓️", callback_data="Virgo"),
        InlineKeyboardButton(text="♒️", callback_data="Libra"),
        InlineKeyboardButton(text="♑️", callback_data="Scorpio")
    ],
    [
        InlineKeyboardButton(text="♐️", callback_data="Sagittarius"),
        InlineKeyboardButton(text="♏️", callback_data="Capricorn"),
        InlineKeyboardButton(text="♎️", callback_data="Aquarius"),
        InlineKeyboardButton(text="♍️", callback_data="Pisces")
    ],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

'''
1. При регистрации бот предлагает пользователю выбрать свой знак зодиака. Используется ReplyKeyboardMarkup 3 ряда по 4 кнопки 
с эмоджи знака зодиака. После выбора знака бот присылает сообщение с информацией о выбранном знаке.
'''
'''♈️ ♉️ ♊️ ♋️ ♌️ ♓️ ♒️ ♑️ ♐️ ♏️ ♎️ ♍️'''

menu = [
    [
        InlineKeyboardButton(text="♈️", callback_data="♈️"),
        InlineKeyboardButton(text="♉️", callback_data="♉️"),
        InlineKeyboardButton(text="♊️", callback_data="♊️"),
        InlineKeyboardButton(text="♋️", callback_data="♋️")
    ],
    [
        InlineKeyboardButton(text="♌️", callback_data="♌️"),
        InlineKeyboardButton(text="♓️", callback_data="♓️"),
        InlineKeyboardButton(text="♒️", callback_data="♒️"),
        InlineKeyboardButton(text="♑️", callback_data="♑️")
    ],
    [
        InlineKeyboardButton(text="♐️", callback_data="♐️"),
        InlineKeyboardButton(text="♏️", callback_data="♏️"),
        InlineKeyboardButton(text="♎️", callback_data="♎️"),
        InlineKeyboardButton(text="♍️", callback_data="♍️")
    ],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
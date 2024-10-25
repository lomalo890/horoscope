from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
import text
import kb
from parsing import parsing_description
import config

router = Router()
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

zodiac_info = {
    '♈️': ['Овен: Энергичные и уверенные в себе.', "https://horo.mail.ru/prediction/aries/today/", 1],
    '♉️': ['Телец: Практичные и надежные.','https://horo.mail.ru/prediction/taurus/today/', 2],
    '♊️': ['Близнецы: Общительные и любопытные.', 'https://horo.mail.ru/prediction/gemini/today/', 3],
    '♋️': ['Рак: Чувствительные и заботливые.', 'https://horo.mail.ru/prediction/cancer/today/', 4],
    '♌️': ['Лев: Творческие и харизматичные.', 'https://horo.mail.ru/prediction/leo/today/', 5],
    '♍️': ['Дева: Аналитичные и внимательные.', 'https://horo.mail.ru/prediction/virgo/today/', 6],
    '♎️': ['Весы: Уравновешенные и дипломатичные.', 'https://horo.mail.ru/prediction/libra/today/', 7],
    '♏️': ['Скорпион: Страстные и решительные.', 'https://horo.mail.ru/prediction/scorpio/today/', 8],
    '♐️': ['Стрелец: Оптимистичные и авантюрные.', 'https://horo.mail.ru/prediction/sagittarius/today/', 9],
    '♑️': ['Козерог: Амбициозные и трудолюбивые.', 'https://horo.mail.ru/prediction/capricorn/today/', 10],
    '♒️': ['Водолей: Независимые и оригинальные.', 'https://horo.mail.ru/prediction/aquarius/today/', 11],
    '♓️': ['Рыбы: Чувствительные и интуитивные.', 'https://horo.mail.ru/prediction/pisces/today/', 12]
}

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.callback_query()
async def callback_handler(callback_query: CallbackQuery):
    simbol = callback_query.data
    path = f"images/{zodiac_info[simbol][2]}.png"
    zodiac_about = zodiac_info[simbol][0]
    url = zodiac_info[simbol][1]
    answer = parsing_description(url)
    description = f"{simbol} {zodiac_about}\n\n{answer}"

    print(simbol)
    print(zodiac_about)
    print(answer)
    print(path)

    await callback_query.answer()
    photo = FSInputFile(path, 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo=photo, caption=description)

    
@router.message()
async def message_handler(msg: Message):
    photo = FSInputFile("images/3.png", 'rb')
    await bot.send_photo(msg.chat.id, photo=photo, caption='asdf')
    
















from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import text
import kb

router = Router()

zodiac_info = {
    '♈️': 'Овен: Энергичные и уверенные в себе.',
    '♉️': 'Телец: Практичные и надежные.',
    '♊️': 'Близнецы: Общительные и любопытные.',
    '♋️': 'Рак: Чувствительные и заботливые.',
    '♌️': 'Лев: Творческие и харизматичные.',
    '♍️': 'Дева: Аналитичные и внимательные.',
    '♎️': 'Весы: Уравновешенные и дипломатичные.',
    '♏️': 'Скорпион: Страстные и решительные.',
    '♐️': 'Стрелец: Оптимистичные и авантюрные.',
    '♑️': 'Козерог: Амбициозные и трудолюбивые.',
    '♒️': 'Водолей: Независимые и оригинальные.',
    '♓️': 'Рыбы: Чувствительные и интуитивные.'
}

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.callback_query()
async def callback_handler(callback_query: CallbackQuery):
    simbol = callback_query.data
    print(simbol)
    await callback_query.answer() 
    await callback_query.message.answer(zodiac_info[simbol])
    
@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")













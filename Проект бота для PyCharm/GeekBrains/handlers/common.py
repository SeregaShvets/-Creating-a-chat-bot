from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import logging
import random
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
   name = message.chat.first_name
   await message.answer(f"Привет, {name}", reply_markup=kb1)

@router.message(Command("fox"))
@router.message(F.text. lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
   name = message.chat.first_name
   img_fox = fox()
   await message.answer(f"Держи лису, {name}")
   await message.answer_photo(photo=img_fox)

@router.message(F.text == 'info')
@router.message(Command("info"))
async def cmd_info(message: types.Message):
   await message.reply("Я бот - твой друг и товарищ ")

@router.message(Command("info2"))
async def cmd_info2(message: types.Message):
   number = random.randint(1, 7)
   await message.answer("Я тестовый бот")
   await message.answer(f"Твоё число {number}")

@router.message(F.text.lower() == "stop!")
async def with_puree(message: types.Message):
    await message.reply("Стоп машина!!")

@router.message(F.text.lower() == "start!")
async def without_puree(message: types.Message):
    await message.reply("Поехали!")

@router.message(F.text)
async def msg_echo(message: types.Message):
        msg_user = message.text
        name = message.chat.first_name
        if 'привет' in message.text.lower():
            await message.reply(f"И тебе привет, {name}")
        elif 'стоп' in message.text.lower():
            await message.reply(f"Пока-пока, {name}")
        elif 'ты кто?' in message.text.lower():
            await message.reply(f"Я бот - твой друг и товарищ, {name}")
        elif 'stop' in message.text.lower():
            await message.reply(f"Пока, {name}")
        elif 'кубик' in message.text.lower():
            await message.answer_dice(emoji="")
        elif 'лиса' in message.text.lower():
            await message.reply(f"Смотри, {name}", reply_markup=kb2)
        else:
            await message.reply(f"Я не знаю этого слова, {name}")




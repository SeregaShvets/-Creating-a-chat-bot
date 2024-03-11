from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard


router = Router()

available_prof_names = ["Разработчик", "Аналитик", "Тестировщик"]
available_prof_grades = ["Junior", "Middle", "Senior"]
available_prof_desert = ["Опрос окончен"]

class ChoiceProf_Names(StatesGroup):
   choice_prof_names = State()
   choice_prof_grades = State()


@router.message(Command("prof"))
async def cmd_prof(message: types.Message, state: FSMContext):
   name = message.chat.first_name
   await message.answer(f"Привет, {name}, выбери свою профессию", reply_markup=make_row_keyboard(available_prof_names))
   await state.set_state(ChoiceProf_Names.choice_prof_names)

@router.message(ChoiceProf_Names.choice_prof_names, F.text.in_(available_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext):
   await state.update_data(chosen_prof=message.text.lower())
   await message.answer(f"Теперь выбери свой уровень", reply_markup=make_row_keyboard(available_prof_grades))
   await state.set_state(ChoiceProf_Names.choice_prof_grades)

@router.message(ChoiceProf_Names.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message, state: FSMContext):
   await message.answer(f"Я не знаю такой профессии", reply_markup=make_row_keyboard(available_prof_names))

@router.message(ChoiceProf_Names.choice_prof_grades, F.text.in_(available_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
   user_data = await state.get_data()
   await message.answer(f"Вы выбрали {message.text.lower()} уровень. Ваша професcия{user_data.get("chosen_prof")}",
   reply_markup=types.ReplyKeyboardRemove())
   await state.set_state.clear()

@router.message(ChoiceProf_Names.choice_prof_grades)
async def prof_chosen_incorrectly(message: types.Message, state: FSMContext):
   await message.answer(f"Я не знаю такой уровень", reply_markup=make_row_keyboard(available_prof_grades))
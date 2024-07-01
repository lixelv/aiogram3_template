from aiogram import Router, types  # , F
from aiogram.filters import Command
# from aiogram.enums import ParseMode
# from aiogram.fsm.context import FSMContext

from app.database import db
# from app.filters import Text

# from app.states import BasicState
# from app.keyboards import inline_data
from app.lexer import Lexer

router = Router()
lexer = Lexer()
# region text


@router.message(Command("start"))
async def start(message: types.Message):
    lang = await db.get_lang(message.from_user.id)
    await message.answer(lexer[lang]["start"])


@router.message(Command("help"))
async def help(message: types.Message):
    lang = await db.get_lang(message.from_user.id)
    await message.answer(lexer[lang]["help"])


# endregion

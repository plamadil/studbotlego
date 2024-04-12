#!/opt/studbot/bin/python3.10

import logging
import sqlite3
import types
import time

import aiogram
from aiogram.types import InputFile, ContentType
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.bot.api import TelegramAPIServer
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InlineKeyboardButton, contact
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)

API_TOKEN = '6976515071:AAEoQKuWyo5IpuW257iJex-A2hCAfSxY_VQ'
ADMIN = 417905942
OLEG = 498487337
oleg_chat_id = 0
user_data = {}
#local_server=TelegramAPIServer.from_base('http://localhos')
date = time.strftime('%Y-%m-%d %H-%M')
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER, block INTEGER);""")
conn.commit()


class dialog(StatesGroup):
    send_info = State()
    chosie_task = State()
    send_contact_dev = State()
    send_contact_win = State()
    send_contact_IB = State()
    send_contact_lin = State()


@dp.message_handler(commands=['start'])
async def info(message: types.Message):
    adkb = types.InlineKeyboardMarkup(resize_keyboard=True)
    adkb.add(types.InlineKeyboardButton(text="Дэвы/Разработка", callback_data='dev'))
    adkb.add(types.InlineKeyboardButton(text="Администрирование Windows", callback_data='windows'))
    adkb.add(types.InlineKeyboardButton(text="Практические задания Linux/bsd", callback_data='linux'))
    adkb.add(types.InlineKeyboardButton(text="Проекты ИБ Безопасность", callback_data='IB'))
    await message.answer('Привет Мы получили твою Анкету.Выбери направление', reply_markup=adkb)


@dp.callback_query_handler(lambda c: c.data == 'dev')
async def sev(callback_query: types.CallbackQuery):
    kkb = types.ReplyKeyboardMarkup()
    bbt = types.KeyboardButton('Отправить контакт', request_contact=True)
    kkb.add(bbt)
    await bot.send_message(callback_query.from_user.id,
                           '2001 Развёртка среды LAMP \n2004 Создание телеграм бота на выделенном сервере и интеграция с предыдущими лабораториями \n2002 Наполнение базы / авторизация продолжение \n2003 Наполнение базы данных из авторизированных пользователей продолжение \n2005 модификация системы авторизации на 2х факторную с использованием телеграмм бота \n0000 Изучение лаборатории openvpn esxi \n2005 Создание скриптов на python',reply_markup=kkb)
    await bot.send_photo(callback_query.from_user.id ,"AgACAgIAAxkBAAIBHWV0e547gPxVYvD0AAH7awFxijI-WAACs9QxG-qGqUuTozpUoiH1RwEAAwIAA3kAAzME",reply_markup=kkb)
    await bot.send_message(callback_query.from_user.id,"Отправь карточку контакта")
    await dialog.send_contact_dev.set()


@dp.callback_query_handler(lambda c: c.data == 'windows')
async def win(callback_query: types.CallbackQuery):
    kkb = types.ReplyKeyboardMarkup()
    bbt = types.KeyboardButton('Отправить контакт', request_contact=True)
    kkb.add(bbt)
    await bot.send_message(callback_query.from_user.id,
                           '3001: Разворачивание служб Active Directory и проверка прав доступа \n3002: Разворачивание служб Microsoft Exchange 2019',reply_markup=kkb)
    await bot.send_photo(callback_query.from_user.id ,"AgACAgIAAxkBAAIBG2V0ezl1JAAB_Vpu-ts3TuI2jK0kGQACsdQxG-qGqUsdmKWTZo0cDAEAAwIAA3kAAzME",reply_markup=kkb)
    await bot.send_message(callback_query.from_user.id,"Отправь карточку контакта")
    await dialog.send_contact_win.set()


@dp.callback_query_handler(lambda c: c.data == 'linux')
async def linux(callback_query: types.CallbackQuery):
    kkb = types.ReplyKeyboardMarkup()
    bbt = types.KeyboardButton('Отправить контакт', request_contact=True)
    kkb.add(bbt)
    await bot.send_message(callback_query.from_user.id,
                           '001 Поднять систему мониторинга \n002 установить asterisk. Сделать тестовый телефонный звонок \n 003 Практика Линукс pfsense + win = pfsense + linux клиент \n004 Практика ansible + puppet \n005 развёртка кластера postgress \n006 развертка elastixsearch',reply_markup=kkb)
    await bot.send_photo(callback_query.from_user.id ,"AgACAgIAAxkBAAIBGWV0ek9QgRGMHHc2t00U7qR3rdTzAAKo1DEb6oapS3zSB5Fnvlv3AQADAgADeQADMwQ",reply_markup=kkb)
    await bot.send_message(callback_query.from_user.id,"Отправь карточку контакта")
    await dialog.send_contact_lin.set()


@dp.callback_query_handler(lambda c: c.data == 'IB')
async def IB(callback_query: types.CallbackQuery):

    kkb = types.ReplyKeyboardMarkup()
    bbt = types.KeyboardButton('Отправить контакт', request_contact=True)
    kkb.add(bbt)
    await bot.send_message(callback_query.from_user.id,
                           '1001 Просмотр пакетов при авторизации wireshark \n 1002 Перехватить wifi \n 1003 Произвести сканирование сайта и разобрать отчёт по найденным уязвимостям openVAs,либо nessus \n 1004 сформировать таблицу IP адресов в файле на основе обращений',reply_markup=kkb)
    await bot.send_photo(callback_query.from_user.id ,"AgACAgIAAxkBAAIBE2V0eaOZbhnP1mXnSfYzWkQ57z8IAAKe1DEb6oapSwdSJ15WxfkWAQADAgADeQADMwQ",reply_markup=kkb)
    await bot.send_message(callback_query.from_user.id,"Отправь карточку контакта")
    await dialog.send_contact_IB.set()


@dp.message_handler(state=dialog.send_contact_dev, content_types=types.ContentType.CONTACT)
async def proc(message: types.Message, state: FSMContext):
    await bot.send_contact(OLEG, first_name=message.contact.first_name, last_name=message.contact.last_name, phone_number=message.contact.phone_number)
    await bot.send_message(OLEG, text="dev")
    await state.finish()

@dp.message_handler(state=dialog.send_contact_win, content_types=types.ContentType.CONTACT)
async def proc(message: types.Message, state: FSMContext):
    await bot.send_contact(OLEG, first_name=message.contact.first_name, last_name=message.contact.last_name, phone_number=message.contact.phone_number)
    await bot.send_message(OLEG, text="win")
    await state.finish()

@dp.message_handler(state=dialog.send_contact_IB, content_types=types.ContentType.CONTACT)
async def proc(message: types.Message, state: FSMContext):
    await bot.send_contact(OLEG, first_name=message.contact.first_name, last_name=message.contact.last_name, phone_number=message.contact.phone_number)
    await bot.send_message(OLEG, text="IB")
    await state.finish()

@dp.message_handler(state=dialog.send_contact_lin, content_types=types.ContentType.CONTACT)
async def proc(message: types.Message, state: FSMContext):
    await bot.send_contact(OLEG, first_name=message.contact.first_name, last_name=message.contact.last_name, phone_number=message.contact.phone_number)
    await bot.send_message(OLEG, text="linux")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

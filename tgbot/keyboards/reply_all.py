# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from tgbot.data.config import get_admins
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки главного меню
def menu_frep(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📜 Правила")
    keyboard.row("🗿 Оператор")

    if user_id in get_admins():
        keyboard.row("📊 Статистика")
        keyboard.row("⚙ Настройки", "🔆 Общие функции")

    return keyboard

# Кнопки Правил
def rules():
    rules = InlineKeyboardMarkup(row_width=1)
    rules.add(
           #InlineKeyboardButton(text="Политика Магазина", callback_data="poliShop"),
            InlineKeyboardButton(text="👨‍💻 Правила для клиента ", callback_data="policlient"),
            InlineKeyboardButton(text="📦 Политика ненаходов ", callback_data="policnet"),
            InlineKeyboardButton(text="📑 Политика возрата", callback_data="polimoaney"),
            InlineKeyboardButton(text="📜 Форма Диспута", callback_data="FormaDisp"),
    )
    return rules

# Кнопки платежных систем
def payments_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🥝 Изменить QIWI 🖍", "🥝 Проверить QIWI ♻", "🥝 Баланс QIWI 👁")
    keyboard.row("⬅ Главное меню", "🖲 Способы пополнений")

    return keyboard


# Кнопки общих функций
def functions_frep(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📢 Рассылка")
    keyboard.row("⬅ Главное меню")

    return keyboard


# Кнопки настроек
def settings_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🖍 Изменить данные", "🕹 Выключатели")
    keyboard.row("⬅ Главное меню")

    return keyboard


# Кнопки изменения товаров
def items_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎁 Добавить товары ➕", "🎁 Удалить товары 🖍", "🎁 Удалить все товары ❌")
    keyboard.row("📁 Создать позицию ➕", "📁 Изменить позицию 🖍", "📁 Удалить все позиции ❌")
    keyboard.row("🗃 Создать категорию ➕", "🗃 Изменить категорию 🖍", "🗃 Удалить все категории ❌")
    keyboard.row("⬅ Главное меню")

    return keyboard


# Завершение загрузки товаров
finish_load_rep = ReplyKeyboardMarkup(resize_keyboard=True)
finish_load_rep.row("📥 Закончить загрузку товаров")

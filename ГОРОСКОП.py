
import random

import telebot


bot = telebot.TeleBot("7634265648:AAEgNaDWtjrYrY3zcRPZLPn_447JOO8d7EQ")

from telebot import types


first = [
    "Сегодня — идеальный день для новых начинаний.",
    "Оптимальный день для того, чтобы решиться на смелый поступок!",
    "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
    "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
    "Плодотворный день для того, чтобы разобраться с накопившимися делами. \n Удачного дня приходи завтра!",
]
second = [
    "Но помните, что даже в этом случае нужно не забывать про",
    "Если поедете за город, заранее подумайте про",
    "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
    "Если у вас упадок сил, обратите внимание на",
    "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про. \n Удачного дня приходи завтра!",
]
second_add = [
    "отношения с друзьями и близкими.",
    "работу и деловые вопросы, которые могут так некстати помешать планам.",
    "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
    "бытовые вопросы — особенно те, которые вы не доделали вчера.",
    "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца.",
]
third = [
    "Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
    "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
    "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
    "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
    "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты. \n Удачного дня приходи завтра!",
]



@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    
    
    keyboard = types.InlineKeyboardMarkup()
   
    key_oven = types.InlineKeyboardButton(text="Овен", callback_data="zodiac")
   
    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text="Телец", callback_data="zodiac")
    keyboard.add(key_telec)
    key_bliznecy = types.InlineKeyboardButton(text="Близнецы", callback_data="zodiac")
    keyboard.add(key_bliznecy)
    key_rak = types.InlineKeyboardButton(text="Рак", callback_data="zodiac")
    keyboard.add(key_rak)
    key_lev = types.InlineKeyboardButton(text="Лев", callback_data="zodiac")
    keyboard.add(key_lev)
    key_deva = types.InlineKeyboardButton(text="Дева", callback_data="zodiac")
    keyboard.add(key_deva)
    key_vesy = types.InlineKeyboardButton(text="Весы", callback_data="zodiac")
    keyboard.add(key_vesy)
    key_scorpion = types.InlineKeyboardButton(text="Скорпион", callback_data="zodiac")
    keyboard.add(key_scorpion)
    key_strelec = types.InlineKeyboardButton(text="Стрелец", callback_data="zodiac")
    keyboard.add(key_strelec)
    key_kozerog = types.InlineKeyboardButton(text="Козерог", callback_data="zodiac")
    keyboard.add(key_kozerog)
    key_vodoley = types.InlineKeyboardButton(text="Водолей", callback_data="zodiac")
    keyboard.add(key_vodoley)
    key_ryby = types.InlineKeyboardButton(text="Рыбы", callback_data="zodiac")
    keyboard.add(key_ryby)
    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(
        message.from_user.id,
        text=" Привет выбери свой знак зодиака",
        reply_markup=keyboard,
    )
    message.text == "/start"



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    
    if call.data == "zodiac":
       
        msg = (
                random.choice(first)
                + " "
                + random.choice(second)
                + " "
                + random.choice(second_add)
                + " "
                + random.choice(third)
        )
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)

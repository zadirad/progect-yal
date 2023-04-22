# -*- coding: utf-8 -*-Я
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('5667650235:AAH_0njpmmveDdZ0mDSXlXAj2NdCxV4nRZA')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["мы ещё не готовы показать билд данного персонажа"]
second = ["простите ); разработка персонажа только началась"]
second_add = [""]
third = ["персонаж ещё не готов. пожалйста подождите"]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали
    if message.text == "Билды":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Выбери персонажа на которого хочешь посмотреть билд")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_haitam = types.InlineKeyboardButton(text='🌿Аль Хайтам🌿', callback_data='haitam')
        # И добавляем кнопку на экран
        keyboard.add(key_haitam)
        key_ganui = types.InlineKeyboardButton(text='❄Гань Юй❄', callback_data='ganui')
        keyboard.add(key_ganui)
        key_raiden = types.InlineKeyboardButton(text='⚡️Райден⚡️', callback_data='raiden')
        keyboard.add(key_raiden)
        key_nahida = types.InlineKeyboardButton(text='🌿Нахида🌿', callback_data='nahida')
        keyboard.add(key_nahida)
        key_ayaka = types.InlineKeyboardButton(text='❄Аяка❄', callback_data='ayaka')
        keyboard.add(key_ayaka)
        key_strannik = types.InlineKeyboardButton(text='༄Странник༄', callback_data='strannik')
        keyboard.add(key_strannik)
        key_hutava = types.InlineKeyboardButton(text='🔥Ху Тао🔥', callback_data='hutava')
        keyboard.add(key_hutava)
        key_kakome = types.InlineKeyboardButton(text='💧Кокоми💧', callback_data='kakome')
        keyboard.add(key_kakome)
        key_xiao = types.InlineKeyboardButton(text='༄Сяо༄', callback_data='xiao')
        keyboard.add(key_xiao)
        key_shenhe = types.InlineKeyboardButton(text='❄Шень Хе❄', callback_data='shenhe')
        keyboard.add(key_shenhe)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Билды персонажей которые имеются', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Здравствуйте напишите Билды")
    else:
        bot.send_message(message.from_user.id, "чтобы посмотреть сборку на персонажа напиши: Билды")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "haitam":
        msg = "Вы открыли персонажа: 🌿Аль Хайтам🌿"
        weapon = "⚔️ОРУЖИЕ⚔️"
        sss = "конечно же лучше всего подойдет его сигнатурное оружие:🌿Свет лиственного разреза🌿 5⭐, но подойдут такие варианты как: 🌿Драгоценный омут🌿 5⭐, 💧Харан💧 5⭐, ✨Рассекающий туман✨ 5⭐ и         🌀Клятва свободы🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        ajs = "Лучшим сетом артефактов является: 🌳Воспоминания дремучего леса🌳 , но также советую расмотреть ☀️Позолоченные сны☀️ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, sss)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, ajs)

    if call.data == "ganui":
        m = "Вы открыли персонажа: ❄️Гань Юй ❄"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ss = "конечно же лучше всего подойдет её сигнатурное оружие:Лук Амоса 5⭐, но подойдут такие варианты как: 🌿Охотничья тропа🌿 5⭐, 💧Аква симулякрум💧 5⭐, ✨Громовой пульс✨ 5⭐ и         🌀Небесное Крыло🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        aj = "Лучшим сетом артефактов является: 🌳Странствуйщий Ансабль🌳 , но также советую расмотреть ☀️Сименава☀️ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, m)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ss)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, aj)

    if call.data == "raiden":
        ra = "Вы открыли персонажа: ⚡️Райден⚡️"
        weapon = "⚔️ОРУЖИЕ⚔️"
        id = "конечно же лучше всего подойдет её сигнатурное оружие:⚡Сияющая Жатва ⚡5⭐, но подойдут такие варианты как: 🌿Улов🌿 4⭐, 🌀Посох Алых Песков🌀 5⭐, ✨Посох Хомы✨ 5⭐"
        artef = "☄️АРТЕФАКТЫ☄️"
        en = "Лучшим сетом артефактов является: ✨Эмблема рассечённой судьбы✨ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, ra)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, id)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, en)

    if call.data == "nahida":
        na = "Вы открыли персонажа: 🌿Нахида🌿"
        weapon = "⚔️ОРУЖИЕ⚔️"
        hi = "конечно же лучше всего подойдет её сигнатурное оружие:🌿Сновидения тысячи ночей🌿5⭐, но подойдут такие варианты как: 🌿Истина Кагура🌿 5⭐, 🌀Молитва святым ветрам🌀 5⭐, ✨Небесный атлас✨ 5⭐"
        artef = "☄️АРТЕФАКТЫ☄️"
        da = "Лучшим сетом артефактов является: ✨Воспоминания дремучего леса✨ , но также хорошо втанет ⭐Позолоченные сны⭐"
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, na)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, hi)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, da)

    if call.data == "ayaka":
        ay = "Вы открыли персонажа: ❄Аяка❄"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ak = "конечно же лучше всего подойдет её сигнатурное оружие:✨Рассекающий туман✨ 5⭐, но подойдут такие варианты как: 🌿Драгоценный омут🌿 5⭐, 💧Харан💧 5⭐, 🌿Свет лиственного разреза🌿 5⭐ и         🌀Клятва свободы🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        va = "Лучшим сетом артефактов является: ❄Заблудший в метели ❄, но также на первое время подойдет ☀️Конец гладиатора☀"
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, ay)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ak)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, va)

    if call.data == "strannik":
        ay = "Вы открыли персонажа: ༄Странник༄"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ak = "конечно же лучше всего подойдет его сигнатурное оружие:✨Воспоминания Тулайтуллы✨ 5⭐, но подойдут такие варианты как: 🌿Истина Кагура	🌿 5⭐, 💧Небесный атлас💧 5⭐, 🌿Молитва святым ветрам🌿 5⭐ и         🌀Память о пыли🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        a = "Лучшим сетом артефактов является: ✨Память о пыли ✨, но также на первое время подойдет ☀Хроники Чертогов в пустыне☀ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, ay)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ak)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, a)

    if call.data == "hutava":
        hu = "Вы открыли персонажа: 🔥Ху Тао🔥"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ta = "конечно же лучше всего подойдет её сигнатурное оружие:✨Посох Хомы✨ 5⭐, но подойдут такие варианты как: 🌿Истина Кагура	🌿 5⭐, 💧Небесный атлас💧 5⭐, 🌿Молитва святым ветрам🌿 5⭐ и         🌀Память о пыли🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        va = "Лучшим сетом артефактов является: ❄Горящая алая ведьма ❄, но также на первое время подойдет ☀воспоминание сименавы   ☀ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, hu)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ta)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, va)

    if call.data == "kakome":
        ka = "Вы открыли персонажа: 💧Кокоми💧"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ko = "конечно же лучше всего подойдет его сигнатурное оружие:✨Вечное лунное сияние✨ 5⭐, но подойдут такие варианты как: 🌿Прототип: Янтарь🌿 5⭐, 💧Морской атлас💧 5⭐, 🌿Морской атлас🌿 5⭐ и         🌀Руководство по магии🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        me = "Лучшим сетом артефактов является: ❄Моллюск морских красок❄, но также на первое время подойдет ☀Стойкость Миллелита☀ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, ka)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ko)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, me)

    if call.data == "xiao":
        x = "Вы открыли персонажа: ༄Сяо༄"
        weapon = "⚔️ОРУЖИЕ⚔️"
        ia = "конечно же лучше всего подойдет его сигнатурное оружие:✨Нефритовый коршун✨ 5⭐, но подойдут такие варианты как: 🌿Посох Хомы🌿 5⭐, 💧Небесная ось💧 5⭐, 🌿Черногорская пика🌿 5⭐ и         🌀Смертельный бой🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        o = "Лучшим сетом артефактов является: ❄Киноварное загробье❄, но также на первое время подойдет ☀Хроники Чертогов в пустыне☀ "
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, x)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, ia)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, o)

    if call.data == "shenhe":
        sh = "Вы открыли персонажа: ❄Шень Хе❄"
        weapon = "⚔️ОРУЖИЕ⚔️"
        en = "конечно же лучше всего подойдет её сигнатурное оружие:✨Усмиритель бед✨ 5⭐, но подойдут такие варианты как: 🌿Небесная ось🌿 5⭐, 💧Покоритель вихря💧 5⭐, 🌿Сияющая жатва🌿 5⭐ и         🌀Посох Хомы🌀 5⭐."
        artef = "☄️АРТЕФАКТЫ☄️"
        he = "Лучшим сетом артефактов является: 2 + 2 из Конец гладиатора/Воспоминания Симэнавы/Киноварное загробье/Отголоски подношения"
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, sh)
        bot.send_message(call.message.chat.id, weapon)
        bot.send_message(call.message.chat.id, en)
        bot.send_message(call.message.chat.id, artef)
        bot.send_message(call.message.chat.id, he)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
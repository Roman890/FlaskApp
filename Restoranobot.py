from Templates import Templates_Restoranobot
from config import api_id, api_hash
from telethon import TelegramClient
import time
from datetime import date
import asyncio

def check_RestoranoBotStart(channel_username):
    """Проверка start для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_3():
            return "Error in >Чем я могу Вам помочь?.."
        if msgs[1].to_dict()['message'] != Templates_Restoranobot.answer_2():
            return "Error in >Вас приветствует чат-бот..."
        if msgs[2].to_dict()['message'] != Templates_Restoranobot.answer_1():
            return "Error in >Фото при старте бота."
        return "Completed successfully"


def check_RestoranoBotContacts(channel_username):
    """Проверка 📱 Контакты 📱 для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '📱 Контакты 📱'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_contacts()[0]:
            return "Error in >Будем ждать Вас.."
        if msgs[1].to_dict()['message'] != Templates_Restoranobot.answer_for_contacts()[1]:
            return "Error in >Наш адрес..."
        if msgs[2].to_dict()['message'] != Templates_Restoranobot.answer_for_contacts()[2]:
            return "Error in >Фото адреса..."
        return "Completed successfully"


def check_RestoranoBotElectronicCard(channel_username):
    """Проверка 💳 Электронная карта 💳 для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '💳 Электронная карта 💳'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_electronic_card()[0]:
            return "Error in >QR-код..."
        if msgs[1].to_dict()['message'] != Templates_Restoranobot.answer_for_electronic_card()[1]:
            return "Error in >Покажите этот QR-код..."
        return "Completed successfully"


def check_RestoranoBotMenu(channel_username):
    """Проверка 🥣 Посмотреть Меню 🍹 для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '🥣 Посмотреть Меню 🍹'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_menu_step1()[0]:
            return "Error in >Что Вас интересует?.."
        if msgs[1].to_dict()['message'] != Templates_Restoranobot.answer_for_menu_step1()[1]:
            return "Error in >(Обложка меню)..."
        client.loop.run_until_complete(client.send_message(channel_username, '🥣 Мясные блюда 🍛'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_menu_step1()[1]:
            return "Error in >(Мясное меню)..."
        client.loop.run_until_complete(client.send_message(channel_username, '💫 Другой раздел меню 💫'))
        time.sleep(20)
        client.loop.run_until_complete(client.send_message(channel_username, '🍸 Суши и роллы 🍹'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_menu_step1()[1]:
            return "Error in >(Суши и ролы меню)..."
        client.loop.run_until_complete(client.send_message(channel_username, '💫 Другой раздел меню 💫'))
        time.sleep(20)
        client.loop.run_until_complete(client.send_message(channel_username, '🍷 Дополнительное 🥂'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_menu_step1()[1]:
            return "Error in >(Дополнительное меню)..."
        return "Completed successfully"



def check_RestoranoBotFotos(channel_username):
    """Проверка 📸 Фотогалерея 📸 для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '📸 Фотогалерея 📸'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_fotos()[0]:
            return "Error in >Хотим поделиться..."
        if msgs[1].to_dict()['message'] != Templates_Restoranobot.answer_for_fotos()[1]:
            return "Error in >(1-ое видео)..."
        client.loop.run_until_complete(client.send_message(channel_username, '📸 Смотреть фото 📸'))
        time.sleep(30)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_fotos()[1]:
            return "Error in >(фотогалерея).."
        return "Completed successfully"


def check_RestoranoBotTableReservations(channel_username):
    """Проверка ✨ Забронировать столик ✨ для @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '✨ Забронировать столик ✨'))
        time.sleep(15)
        client.loop.run_until_complete(client.send_message(channel_username, '2'))
        time.sleep(15)
        today = date.today()
        client.loop.run_until_complete(client.send_message(channel_username, today.strftime("%d/%m/%Y")))
        time.sleep(15)
        current_time = time.localtime()
        client.loop.run_until_complete(client.send_message(channel_username, time.strftime("%H:%M", current_time)))
        time.sleep(15)
        client.loop.run_until_complete(client.send_message(channel_username, "Артем"))
        time.sleep(15)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=10))
        if msgs[0].to_dict()['message'] != Templates_Restoranobot.answer_for_table_reservation()[0]:
            return "Error in >Столик успешно забронирован."
        if msgs[2].to_dict()['message'] != Templates_Restoranobot.answer_for_table_reservation()[1]:
            return "Error in >На чье имя будет бронирование..."
        if msgs[4].to_dict()['message'] != Templates_Restoranobot.answer_for_table_reservation()[2]:
            return "Error in >Укажите время..."
        if msgs[6].to_dict()['message'] != Templates_Restoranobot.answer_for_table_reservation()[3]:
            return "Error in >Укажите дату..."
        if msgs[8].to_dict()['message'] != Templates_Restoranobot.answer_for_table_reservation()[4]:
            return "Error in >На сколько человек..."
        return "Completed successfully"


def check_RestoranoBot_return_to_mainMenu(channel_username):
    """Вернуться в главное меню @Restoranobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '🔼 Вернуться в главное меню 🔼'))


def all_message(channel_username, number):
    """просмотр сообщений в телеграм"""
    loop = asyncio.new_event_loop()
    with TelegramClient('sessions/session6', api_id, api_hash, loop=loop) as client:
        row_msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=number))
        msgs = []
        for msg in row_msgs:
            msgs.append(msg.to_dict()['message'])
        return msgs


def run_restoranobot_tests(number, channel_username):
    """Функция запуска тестов для бота @Restoranobot"""
    number = int(number)
    if number == 601:
        # проверка команды /start
        return check_RestoranoBotStart(channel_username)
    elif number == 602:
        # проверка просмотра контактов
        log = check_RestoranoBotContacts(channel_username)
        check_RestoranoBot_return_to_mainMenu(channel_username)
        return log
    elif number == 603:
        # проверка просмотра меню
        log = check_RestoranoBotMenu(channel_username)
        check_RestoranoBot_return_to_mainMenu(channel_username)
        return log
    elif number == 604:
        # проверка электронной карты
        log = check_RestoranoBotElectronicCard(channel_username)
        check_RestoranoBot_return_to_mainMenu(channel_username)
        return log
    elif number == 605:
        # проверка бронирования столика
        log = check_RestoranoBotTableReservations(channel_username)
        check_RestoranoBot_return_to_mainMenu(channel_username)
        return log
    elif number == 606:
        # проверка фотогалереи
        log = check_RestoranoBotFotos(channel_username)
        check_RestoranoBot_return_to_mainMenu(channel_username)
        return log
    elif number == 607:
        # проверка доставки блюд
        return
    elif number == 608:
        # проверка вызова персонала
        return
    elif number == 609:
        # проверка рекомендации другу
        return
    elif number == 610:
        # проверка видеоселфи
        return
    else :
        return

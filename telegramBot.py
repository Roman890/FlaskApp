from telethon import TelegramClient
import time
import asyncio
from config import api_id, api_hash
from Templates import \
    Templates_AcademyPickBot,\
    Templates_hi_prof_bot, \
    Templates_kurtsevobot,\
    Templates_DadiRestBot, \
    Templates_TourPickBot

def time_is_out(msg):
    error = f"Error: Время ожидания сообщения:'{msg}', завершилось!"
    return error


def check_AcademyPickBot(channel_username):
    """Проверка положительного сценари для @AcademyPickBot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_time = time.time()
    flag = False
    with TelegramClient('sessions/session1', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))# сообщения
        if msgs[0].to_dict()['message'] != Templates_AcademyPickBot.answer_3():
            return time_is_out("Снимите или загрузите видео...")
        if msgs[1].to_dict()['message'] != Templates_AcademyPickBot.answer_2():
            return time_is_out("Давайте попробуем вместе...")
        if msgs[2].to_dict()['message'] != Templates_AcademyPickBot.answer_1():
            return time_is_out("Приветствую Вас!...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_AcademyPickBot.answer_4():
            return time_is_out("Сделайте и отправьте селфи...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_AcademyPickBot.answer_5():
            return time_is_out("Прикрепите еще одно селфи...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_AcademyPickBot.answer_6():
            return time_is_out("Придумайте подпись к селфи...")
        client.loop.run_until_complete(client.send_message(channel_username, 'Это было круто'))
        time.sleep(20)
        end_time = time.time() - start_time
        while end_time < 420: # 7 минут положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'] == Templates_AcademyPickBot.answer_10():
                flag = True
                break
        if flag:
            msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
            if msgs[0].to_dict()['message'] != Templates_AcademyPickBot.answer_10():
                return "Error:👌 Видеоролик готов!"
            if msgs[1].to_dict()['message'] != Templates_AcademyPickBot.answer_9():
                return "Error:(Видео)"
        else:
            return "Error:Время ожидания видео и заключительного сообщения завершилось!"
        return "Completed successfully"


def check_hi_prof_bot(channel_username):
    """Проверка положительного сценари для @hi_prof_bot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_time = time.time()
    flag = False
    with TelegramClient('sessions/session2', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_hi_prof_bot.answer_1():
            return time_is_out(" Привет👋...")
        client.loop.run_until_complete(client.send_message(channel_username, 'Сделать видео "Первый урок вождения"'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_hi_prof_bot.answer_2():
            return time_is_out("Выберите формат..")    
        client.loop.run_until_complete(client.send_message(channel_username, 'Вертикальное'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_hi_prof_bot.answer_5():
            return time_is_out("Снимите или загрузите видео...")
        if msgs[1].to_dict()['message'] != Templates_hi_prof_bot.answer_4():
            return time_is_out("Итак, приступим...")
        if msgs[2].to_dict()['message'] != Templates_hi_prof_bot.answer_3():
            return time_is_out("Нам понадобится...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_hi_prof_bot.answer_6():
            return time_is_out("Сделайте и отправьте селфи...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        end_time = time.time() - start_time
        while end_time < 420: # 7 минут положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'][:21] == Templates_hi_prof_bot.answer_10():
                flag = True
                break
        if flag:
            msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
            if msgs[0].to_dict()['message'][:21] != Templates_hi_prof_bot.answer_10():
                return "Error:👌 Видеоролик готов!"
            if msgs[1].to_dict()['message'] != Templates_hi_prof_bot.answer_9():
                return "Error:(Видео)"
        else:
            return "Error:Время ожидания видео и заключительного сообщения завершилось!"
        return "Completed successfully"


def check_kurtsevobot(channel_username):
    """Проверка положительного сценари для @kurtsevobot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_time = time.time()
    flag = False
    with TelegramClient('sessions/session3', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_kurtsevobot.answer_3():
            return time_is_out("Загрузите небольшое...")
        if msgs[1].to_dict()['message'] != Templates_kurtsevobot.answer_2():
            return time_is_out("Давайте попробуем вместе...")
        if msgs[2].to_dict()['message'] != Templates_kurtsevobot.answer_1():
            return time_is_out("Приветствую Вас!...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_kurtsevobot.answer_4():
            return time_is_out("Загрузите свое фото...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        end_time = time.time() - start_time
        while end_time < 420: # 7 минут положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'] == Templates_kurtsevobot.answer_8():
                flag = True
                break
        if flag:
            msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
            if msgs[0].to_dict()['message'] != Templates_kurtsevobot.answer_8():
                return "Error:👌 Видеоролик готов!"
            if msgs[1].to_dict()['message'] != Templates_kurtsevobot.answer_7():
                return "Error:(Видео)"
        else:
            return "Error:Время ожидания видео и заключительного сообщения завершилось!"
        return "Completed successfully"


def check_DadiRestBot(channel_username):
    """Проверка положительного сценари для @DadiRestBot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_time = time.time()
    flag = False
    with TelegramClient('sessions/session4', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
        if msgs[0].to_dict()['message'] != Templates_DadiRestBot.answer_2():
            return time_is_out("Чем я могу Вам помочь?...")
        if msgs[1].to_dict()['message'] != Templates_DadiRestBot.answer_1():
            return time_is_out("Привет!...")
        client.loop.run_until_complete(client.send_message(channel_username, '🎬 Сделать видеоселфи 🎬'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_DadiRestBot.answer_5():
            return time_is_out("Снимите/загрузите короткое видео...")
        if msgs[1].to_dict()['message'] != Templates_DadiRestBot.answer_4():
            return time_is_out("Итак, нам понадобится...")
        if msgs[2].to_dict()['message'] != Templates_DadiRestBot.answer_3():
            return time_is_out("👐 Давайте вместе...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_DadiRestBot.answer_6():
            return time_is_out("Отлично! 🤳 ...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        end_time = time.time() - start_time
        while end_time < 420: # 7 минут положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'] == Templates_DadiRestBot.answer_10():
                flag = True
                break
        if flag:
            msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
            if msgs[0].to_dict()['message'] != Templates_DadiRestBot.answer_10():
                return "Error:👌 Видео готово!"
            if msgs[1].to_dict()['message'] != Templates_DadiRestBot.answer_9():
                return "Error:(Видео)"
        else:
            return "Errorr:Время ожидания видео и заключительного сообщения завершилось!"
        return "Completed successfully"



def check_TourPickBot(channel_username):
    """Проверка положительного сценари для @TourPickBot"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_time = time.time()
    flag = False
    with TelegramClient('sessions/session5', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))
        if msgs[0].to_dict()['message'] != Templates_TourPickBot.answer_3():
            return time_is_out("Снимите видео...")
        if msgs[1].to_dict()['message'] != Templates_TourPickBot.answer_2():
            return time_is_out("Давайте попробуем вместе...")
        if msgs[2].to_dict()['message'] != Templates_TourPickBot.answer_1():
            return time_is_out("Приветствую Вас!...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_TourPickBot.answer_4():
            return time_is_out("Прикрепите и оправьте селфи...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_TourPickBot.answer_5():
            return time_is_out("Напишите подпись к селфи...")
        client.loop.run_until_complete(client.send_message(channel_username, 'Это было круто'))
        time.sleep(20)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
        if msgs[0].to_dict()['message'] != Templates_TourPickBot.answer_6():
            return time_is_out("Прикрепите еще одно селфи...")
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(20)
        end_time = time.time() - start_time
        while end_time < 420: # 7 минут положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'] == Templates_TourPickBot.answer_10():
                flag = True
                break
        if flag:
            msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=2))
            if msgs[0].to_dict()['message'] != Templates_TourPickBot.answer_10():
                return "Error:👌Видеоролик готов!"
            if msgs[1].to_dict()['message'] != Templates_TourPickBot.answer_9():
                return "Error:(Видео)"
        else:
            return "Error:Время ожидания видео и заключительного сообщения завершилось!"
        return "Completed successfully"


def all_message(channel_username, number):
    """просмотр сообщений в телеграм"""
    loop = asyncio.new_event_loop()
    with TelegramClient('sessions/all', api_id, api_hash, loop=loop) as client:
        row_msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=number))
        msgs = []
        for msg in row_msgs:
            msgs.append(msg.to_dict()['message'])
        return msgs


def send_errors_in_bot(inveite_link, text):
    """отправление ошибок в ботах в телеграм канал"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient('sessions/errors', api_id, api_hash, loop=loop) as client:
        channel = client.loop.run_until_complete(client.get_entity(inveite_link))
        client.loop.run_until_complete(client.send_message(channel, text))


def run(number, channel_username):
    """Функция запуска тестов"""
    number = int(number)
    if number == 101:
        return check_AcademyPickBot(channel_username)
    elif number == 201:
        return check_hi_prof_bot(channel_username)
    elif number == 301:
        return check_kurtsevobot(channel_username)
    elif number == 401:
        return check_DadiRestBot(channel_username)
    elif number == 501:
        return check_TourPickBot(channel_username)
    else :
        return


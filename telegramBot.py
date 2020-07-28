# -*- coding: utf-8 -*- 
from telethon import TelegramClient
import time
import asyncio
from Templates import Templates, api_id, api_hash, channel_username


def checkComand(channel_username):
    loop = asyncio.new_event_loop()
    with TelegramClient('new', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(2)
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=3))# один последний объект сообщения
        if msgs[2].to_dict()['message'] != Templates.answer_1():
            return "Error in >Приветствую Вас!..."
        if msgs[1].to_dict()['message'] != Templates.answer_2():
            return "Error in >Давайте попробуем вместе..."
        if msgs[0].to_dict()['message'] != Templates.answer_3():
            return "Error in >Снимите или загрузите видео..."
        return "Completed successfully"



def sendAll(channel_username):
    loop = asyncio.new_event_loop()
    start_time = time.time()
    with TelegramClient('new', api_id, api_hash, loop=loop) as client:
        client.loop.run_until_complete(client.send_message(channel_username, '/start'))
        time.sleep(2)
        client.loop.run_until_complete(client.send_file(channel_username, 'static/video/vid.mp4'))
        time.sleep(4)
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(4)
        client.loop.run_until_complete(client.send_file(channel_username, 'static/img/cars.jpg'))
        time.sleep(2)
        client.loop.run_until_complete(client.send_message(channel_username, 'Это было круто'))
        end_time = time.time() - start_time
        while end_time < 240: # 4 минуты положительный сценарий
            msg = client.loop.run_until_complete(client.get_messages(channel_username, limit=1))
            end_time = time.time() - start_time
            if msg[0].to_dict()['message'] == Templates.answer_10():
                return True
        return False



def checkAll(channel_username):
    loop = asyncio.new_event_loop()
    with TelegramClient('new', api_id, api_hash, loop=loop) as client:
        msgs = client.loop.run_until_complete(client.get_messages(channel_username, limit=15))# один последний объект сообщения
        if msgs[14].to_dict()['message'] != Templates.answer_1():
            return "Error in >Приветствую Вас!..."
        if msgs[13].to_dict()['message'] != Templates.answer_2():
            return "Error in >Давайте попробуем вместе..."
        if msgs[12].to_dict()['message'] != Templates.answer_3():
            return "Error in >Снимите или загрузите видео..."
        if msgs[10].to_dict()['message'] != Templates.answer_4():
            return "Error in >Сделайте и отправьте селфи..."
        if msgs[8].to_dict()['message'] != Templates.answer_5():
            return "Error in >Прикрепите еще одно селфи..."
        if msgs[6].to_dict()['message'] != Templates.answer_6():
            return "Error in >Придумайте подпись к селфи..."
        if msgs[4].to_dict()['message'] != Templates.answer_7():
            return "Error in >Видеоролик в процессе монтажа..."
        if msgs[3].to_dict()['message'] != Templates.answer_8() and msgs[2].to_dict()['message'] != Templates.answer_8():
            return "Error in >В работе..."
        if msgs[1].to_dict()['message'] != Templates.answer_9():
            return "Error in >(Видео)"
        if msgs[0].to_dict()['message'] != Templates.answer_10():
            return "Error in >👌 Видеоролик готов!"
        return "Completed successfully"


#print(checkComand(channel_username))
#print(checkAll(channel_username))
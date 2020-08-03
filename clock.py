# -*- coding: utf-8 -*- 
from telegramBot import checkComand, checkAll, sendAll, checkNewAll
from Templates import sms_api, phone_number, all_numbers
from sqlalchemy import desc
import requests
from __init__ import Bots, Logs, db
import time


def sendMessage(text):
    """Отправка смс себе через сервис sms ru"""
    url = f"https://sms.ru/sms/send?api_id={sms_api}&to={all_numbers}&msg={text}&json=1"
    res = requests.get(url)


def mainTests():
    """Проведение тестов для каждого бота"""
    all_bots = Bots.query.all()
    for bot in all_bots:
        for test in bot.tests:
            checkAllTests(test.id, bot.name)
            checkMessage(test.id, bot.name)
            time.sleep(10)


def checkAllTests(id, name):
    if id == 1:
        log = checkComand(name)
        LogsDb(log, id)
    elif id == 2:
        log = checkNewAll(name)
        LogsDb(log, id)
    else :
        LogsDb("Not yet", id)


def LogsDb(text, id):
    """Вставляем данные логов в базу"""
    test_id = id
    my_data = Logs(text, test_id)
    db.session.add(my_data)
    db.session.commit()


def checkMessage(id, name):
    all_logs = Logs.query.filter(Logs.test_id == int(id)).order_by(desc(Logs.id))
    all = Logs.query.filter(Logs.test_id == int(id)).count()
    if all > 1:
        log_1 = all_logs[0].text
        log_2 = all_logs[1].text
        if (log_1 == "Completed successfully") and (log_2 != "Completed successfully"):
            text = f"Бот {name} возобновил работу"
            sendMessage(text)
            return
        elif (log_1 != "Completed successfully") and (log_2 == "Completed successfully"):
            text = f"Внимание!!! Бот {name} не работает"
            sendMessage(text)
            return
        else:
            return


def timed_job():
    mainTests()

timed_job()
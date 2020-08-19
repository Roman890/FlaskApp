from telegramBot import run, send_errors_in_bot
from config import sms_api, all_numbers, inveite_link
from sqlalchemy import desc
import requests
from helpers import Bots, Logs, db
import time
import sys


def runTests(bot_id):
    """Проведение тестов для каждого бота"""
    bot = Bots.query.get(bot_id)
    for test in bot.tests:
        checkAllTests(test.id, bot.name)
        checkMessage(test.id, bot.name)
        time.sleep(10)


def checkAllTests(test_id, name):
    test_id = int(test_id)
    if test_id == 101:
        log = run(test_id, name)
        LogsDb(log, test_id)
    elif test_id == 201:
        log = run(test_id, name)
        LogsDb(log, test_id)
    elif test_id == 301:
        log = run(test_id, name)
        LogsDb(log, test_id)
    elif test_id == 401:
        log = run(test_id, name)
        LogsDb(log, test_id)
    elif test_id == 501:
        log = run(test_id, name)
        LogsDb(log, test_id)
    else :
        LogsDb("Not yet", test_id)


def LogsDb(text, id):
    """Вставляем данные логов в базу"""
    test_id = id
    my_data = Logs(text, test_id)
    db.session.add(my_data)
    db.session.commit()


def sendMessage(text):
    """Отправка смс себе через сервис sms ru и отправка ошибок в telegram-бот"""
    #url = f"https://sms.ru/sms/send?api_id={sms_api}&to={all_numbers}&msg={text}&json=1"
    #res = requests.get(url)
    send_errors_in_bot(inveite_link, text)


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
            text = f"Внимание!!! Бот {name} не работает.\n{log_1}"
            sendMessage(text)
            return
        else:
            return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        runTests(int(sys.argv[1]))
    else:
        exit()
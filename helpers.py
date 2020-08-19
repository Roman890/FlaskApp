# -*- coding: utf-8 -*-
from __init__ import Bots, Tests, Logs, db
from sqlalchemy import desc, asc


def find_logs_from_bots():
    """Достать ботов, тесты и 3 лога из каждого теста"""
    data = {}
    tests = {}
    bots = Bots.query.order_by(asc(Bots.id)).all()
    for bot in bots:
        tests_from_bots = Tests.query.filter(Tests.bot_id == bot.id)
        for test in tests_from_bots:
            logs_from_test = Logs.query.filter(Logs.test_id == int(test.id)).order_by(desc(Logs.id)).limit(3).all()[::-1]
            tests[test] = logs_from_test
            data[bot] = tests
        tests = {}
    return data
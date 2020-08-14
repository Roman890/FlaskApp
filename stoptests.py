from crontab import CronTab

def createCron(bot_id):
    my_cron = CronTab(user=True)
    command = 'cd /var/www/FlaskApp/FlaskApp && sudo python3 runtestscron.py ' + str(bot_id)	
    job = my_cron.new(command=command, comment=str(bot_id))
    job.minute.every(10)
    my_cron.write()
    
def deleteCron(bot_id):
    my_cron = CronTab(user=True)
    for job in my_cron:
        if job.comment == str(bot_id):
            my_cron.remove(job)
            my_cron.write()

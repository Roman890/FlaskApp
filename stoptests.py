from crontab import CronTab

def createCron():
    my_cron = CronTab(user='root')
    command = 'cd /var/www/FlaskApp/FlaskApp && sudo python3 clock.py'	
    job = my_cron.new(command=command, comment='dateinfo')
    job.minute.every(5)
    my_cron.write()
    
def deleteCron():
    my_cron = CronTab(user='root')
    for job in my_cron:
        if job.comment == 'dateinfo':
            my_cron.remove(job)
            my_cron.write()

def pr():
    print("ddddd")

    
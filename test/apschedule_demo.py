from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def my_clock():
    print("hello! Time is:%s" % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # 每3秒执行一次
    # scheduler.add_job(my_clock, "interval", seconds=3)
    # 每天8点40执行任务
    scheduler.add_job(my_clock, 'cron', hour=11, minute=17)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Errors!')

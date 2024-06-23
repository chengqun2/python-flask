# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
#
# from admin_tasks.task import task1, task2
#
#
# # 任务配置类
# class SchedulerConfig:
#     # 配置执行job
#     JOBS = [
#         {
#             'id': 'put_into_queue',
#             'func': task1,
#             'args': None,
#             'trigger': 'interval',
#             'seconds': 3  # 本任务为每3s执行一次
#         },
#         {
#             'id': 'scheduler_dev_queueing',
#             'func': task2,
#             'args': None,
#             'trigger': {  # 本任务为每周一五点五十九分四十秒执行一次
#                 'type': 'cron',  # 类型
#                 'day_of_week': "0",  # 可定义具体哪几天要执行
#                 'hour': '5',  # 小时数
#                 'minute': '59',
#                 'second': '40'  # "*/3" 表示每3秒执行一次，单独一个"3" 表示每分钟的3秒。现在就是每一分钟的第3秒时循环执行。
#             }
#         }
#     ]
#     # 存储位置
#     SCHEDULER_JOBSTORES = {
#         'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
#     }
#     # 线程池配置
#     SCHEDULER_EXECUTORS = {
#         'default': {'type': 'threadpool', 'max_workers': 20}
#     }
#     # 配置时区
#     SCHEDULER_TIMEZONE = 'Asia/Shanghai'
#
#
# SCHEDULER_JOB_DEFAULTS = {
#     'coalesce': False,
#     'max_instances': 3
# }
# # 调度器开关
# SCHEDULER_API_ENABLED = True

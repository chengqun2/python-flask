import os

# from apscheduler.schedulers.background import BackgroundScheduler
# from flask_apscheduler import APScheduler
# from applications.scheduler_config import SchedulerConfig
from flask import Flask
from applications.common.script import init_script
from applications.config import BaseConfig
from applications.extensions import init_plugs
from applications.view import init_bps


def create_app():
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    # 引入配置
    app.config.from_object(BaseConfig)

    # 定时任务
    # app.config.from_object(SchedulerConfig)
    # # 同时指定时区,防止上下时区不一致
    # scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))
    # # 注册app
    # scheduler.init_app(app)
    # scheduler.start()

    # 注册flask组件
    init_plugs(app)

    # 注册蓝图
    init_bps(app)

    # 注册命令
    init_script(app)

    return app

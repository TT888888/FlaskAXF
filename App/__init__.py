from flask import Flask

from App import settings

from App.ext import init_ext

from App.views import init_blue


def craeat_app(env_name):
    app =Flask(__name__)

    # 初始化
    app.config.from_object(settings.config.get(env_name) or 'default')

    # 模块初始化
    init_ext(app=app)

    init_blue(app=app)

    return app
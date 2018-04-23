# 导入第三方包，都放在这里
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session


db = SQLAlchemy()

# 用来做数据迁移用的
migrate=Migrate()

def init_ext(app):
    db.init_app(app=app)

    Session(app=app)

    # 用来做数据迁移用的
    migrate.init_app(app=app,db=db)

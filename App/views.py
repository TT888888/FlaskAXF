
# 蓝图
import random

from flask import Blueprint, render_template

from App.models import Person

from App.ext import db

blue = Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'hello Index'


# 创建表
@blue.route('/createdb/')
def create_db():
    db.create_all()

    return 'su'


# 删除表
@blue.route('/dropdb/')
def drop_db():
    db.drop_all()
    return 'su'




# 添加数据
@blue.route('/addperson/')
def add_person():
    p = Person()

    p.p_age=15
    p.p_name="二狗"

    # 存到数据库
    db.session.add(p)
    db.session.commit()
    return 'su'


# 添加一组数据
@blue.route('/addpersons/')
def add_persons():

    persons=[]

    for i in range(5):
        p=Person()
        p.p_name='haha%d' % random.randrange(100)

        p.p_age = random.randrange(100)
        persons.append(p)

    # 添加一组
    # db.session 会话，和数据库链接的会话
    db.session.add_all(persons)
    db.session.commit()

    print(persons)
    return '添加成功'



# 将数据渲染到Person页面
@blue.route("/getpersons/")
def get_persons():

    # ps=Person.query.all()
    ps = Person.query.filter(Person.p_age > 50)

    return render_template('Person.html',get=ps)


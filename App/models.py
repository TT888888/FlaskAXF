from App.ext import db


class Person(db.Model):

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    p_name=db.Column(db.String(16))
    # 整数，默认值为1
    p_age=db.Column(db.Integer,default=1)

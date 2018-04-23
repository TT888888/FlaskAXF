def get_db_url(dbinfo):
    # 获取信息
    user=dbinfo.get('USER') or "root"
    password = dbinfo.get('PASSWORD') or "123456"
    host = dbinfo.get('HOST') or'127.0.0.1'
    post = dbinfo.get('POST') or '3306'
    name = dbinfo.get('NAME') or 'mysql'

    db = dbinfo.get('DB') or 'mysql'
    driver=dbinfo.get('driver') or 'pymysql'

    return "{}+{}://{}:{}@{}:{}/{}".format(db,driver,user,password,host,post,name)


class Config():

    DEBUG=False
    TESTING=False

    # 被禁用的环境
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# 开发
class DevelopConfig(Config):
    DEBUG = True

    DATABASE={
        'USER':'root',
        "PASSWORD":'123456',
        'HOST':'127.0.0.1',
        'POST':'3306',
        'NAME':'FlaskMysql',
        # 哪一种库
        "DB":'mysql',
        # 驱动
        'driver':'pymysql'
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(DATABASE)



# 测试环境
class TestingConfig(Config):
    TESTING  = True

    DATABASE={
        'USER':'root',
        "PASSWORD":'123456',
        'HOST':'127.0.0.1',
        'POST':'3306',
        'NAME':'FlaskMysql',
        # 哪一种库
        "DB":'mysql',
        # 驱动
        'driver':'pymysql'
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(DATABASE)



# 演示环境
class StaggingConfig(Config):
    DEBUG = True

    DATABASE={
        'USER':'root',
        "PASSWORD":'123456',
        'HOST':'127.0.0.1',
        'POST':'3306',
        'NAME':'FlaskMysql',
        # 哪一种库
        "DB":'mysql',
        # 驱动
        'driver':'pymysql'
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(DATABASE)


# 线上环境
class ProductConfig(Config):
    DEBUG = True

    DATABASE={
        'USER':'root',
        "PASSWORD":'123456',
        'HOST':'127.0.0.1',
        'POST':'3306',
        'NAME':'FlaskMysql',
        # 哪一种库
        "DB":'mysql',
        # 驱动
        'driver':'pymysql'
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(DATABASE)



#选中里面相对的类
config = {
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'stagging':StaggingConfig,
    'product':ProductConfig,
    'default':DevelopConfig
}











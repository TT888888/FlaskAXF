from flask_migrate import MigrateCommand
from flask_script import Manager

from App import craeat_app

app = craeat_app('develop')


manager=Manager(app=app)

# 迁移用
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

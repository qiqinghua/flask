import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}

# 'from app import app 中的第一个 app 是指 app 模块（通常是一个目录）。
# 第二个 app 是指在 app 模块中定义的 Flask 应用实例变量 app。
# 注意，要加上 export FLASK_APP=microblog.py，
# windows 下是set命令，这样flask run就是执行microblog.py这个文件了

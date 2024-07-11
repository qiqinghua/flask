import os
basedir = os.path.abspath(os.path.dirname(__file__)) #basedir: 计算脚本文件所在的绝对路径。这是为了确保数据库文件存储在项目目录中

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # 设置秘密密钥，如果环境变量中未定义，则使用默认值
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') # 设置SQLAlchemy数据库URI，如果环境变量中未定义，则使用SQLite数据库
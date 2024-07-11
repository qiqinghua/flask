from flask import Flask
from config  import Config #从 config.py 文件中导入 Config 类
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  #创建一个Flask应用实例。
app.config.from_object(Config)  #从 Config 类中加载配置。
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes,models  #导入 routes 模块，这里假设你的路由定义在 app/routes.py 文件中
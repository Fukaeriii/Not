import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from app.config import configmodel
import pymysql
db = SQLAlchemy()
def create_app(configname):
    if configname is None:
        configname = os.getenv('FLASK_ENV', 'dev')
     #实例化
    app = Flask(__name__)
    #配置信息
    app.config.from_object(configmodel['dev'])

    #数据库实例化
    db.init_app(app)
    with app.test_request_context():
        from app.Models import user
        db.create_all()
    #Session管理
    Session(app)

    from app.userapi import user
    #注册蓝图
    app.register_blueprint(user, url_prefix='/user')

    return app

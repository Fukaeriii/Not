import redis

class BaseConfig(object):
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ckx1006@localhost:3306/ckx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret string'
    # session配置
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    PERMAENT_SESSION_LIFETIME = 30
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379, db=2)


class DevelopmentConfig(BaseConfig):
    debug = True


configmodel ={
    'dev': DevelopmentConfig
}
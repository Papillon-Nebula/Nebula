from flask import Flask, blueprints,Blueprint



user_bp = Blueprint('users', __name__)


import redis
from flask_sqlalchemy import SQLAlchemy
# 创建db对象
db = SQLAlchemy()
class Config(object):
    DEBUG = True
    SECRET_KEY = "*(%#4sxcz(^(#$#8423"
    # 数据库链接配置:
    #数据类型://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flask_students"
    # 设置mysql的错误跟踪信息显示
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 打印每次模型操作对应的SQL语句
    SQLALCHEMY_ECHO = True

    """把session保存到redis中"""
    # session存储方式为redis
    # SESSION_TYPE="redis"
    # # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    # SESSION_PERMANENT = False
    # # 是否对发送到浏览器上session的cookie值进行加密
    # SESSION_USE_SIGNER = False
    # # 保存到redis的session数的名称前缀
    # SESSION_KEY_PREFIX = "session:"
    # # session保存数据到redis时启用的链接对象
    # SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置

    SESSION_TYPE= 'sqlalchemy'  # session的存储方式为sqlalchemy
    SESSION_SQLALCHEMY= db  # SQLAlchemy对象
    SESSION_SQLALCHEMY_TABLE= 'sessions'  # session要保存的表名称
    SESSION_PERMANENT= True  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER= False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX= 'session:'  # 保存到session中的值的前缀
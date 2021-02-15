# from flask import Flask, blueprints,Blueprint



# user_bp = Blueprint('users', __name__)


# import redis
# from flask_sqlalchemy import SQLAlchemy
# # 创建db对象
# db = SQLAlchemy()
# class Config(object):
#     DEBUG = True
#     SECRET_KEY = "*(%#4sxcz(^(#$#8423"
#     # 数据库链接配置:
#     #数据类型://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称
#     SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flask_students"
#     # 设置mysql的错误跟踪信息显示
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     # 打印每次模型操作对应的SQL语句
#     SQLALCHEMY_ECHO = True

#     """把session保存到redis中"""
#     # session存储方式为redis
#     # SESSION_TYPE="redis"
#     # # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
#     # SESSION_PERMANENT = False
#     # # 是否对发送到浏览器上session的cookie值进行加密
#     # SESSION_USE_SIGNER = False
#     # # 保存到redis的session数的名称前缀
#     # SESSION_KEY_PREFIX = "session:"
#     # # session保存数据到redis时启用的链接对象
#     # SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置

#     SESSION_TYPE= 'sqlalchemy'  # session的存储方式为sqlalchemy
#     SESSION_SQLALCHEMY= db  # SQLAlchemy对象
#     SESSION_SQLALCHEMY_TABLE= 'sessions'  # session要保存的表名称
#     SESSION_PERMANENT= True  # 如果设置为True，则关闭浏览器session就失效。
#     SESSION_USE_SIGNER= False  # 是否对发送到浏览器上session的cookie值进行加密
#     SESSION_KEY_PREFIX= 'session:'  # 保存到session中的值的前缀


from types import MethodType
from typing import Mapping
from flask import Flask
from flask import request, redirect, render_template, session, g, url_for, Blueprint
from dataclasses import dataclass, make_dataclass
from flask.helpers import make_response

from flask.wrappers import Response

app = Flask(__name__)
app.secret_key = '123'

@dataclass
class User():
    id: int
    username: str
    password: str

users = [
    User(1,"mike", "111"),
    User(2,"lilei", "222"),
    User(3,"hanmeimei", "333"),
]

print(users)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [u for u in users if u.id == session['user_id']]
        g.user = user 

@app.route('/login' ,methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user = [u for u in users if u.username== username]
        if len(user)>0:
            user = user[0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('Nebula'))

    return render_template("login.html")


@app.route('/')
def Nebula():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('Nebula.html')


@app.route('/session')
def sess():
    session['islogin'] = 'ture'
    session['username'] = 'papillon-nebula'
    session['nickname'] = 'Sgr A*'
    session['role'] = 'tester'
    return 'Done'

@app.route('/cookie')
def cookie():
    response = make_response('这是cookie的路由')
    response.set_cookie('username', 'papillon-nebula', max_age=30)
    response.set_cookie('password', '111', max_age=30)
    return response

@app.route('/sc/read')
def scread():
    return '你当前的昵称是：%s ' % request.cookies.get('username')



# 定制404错误页
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    from controller.demo import *
    app.register_blueprint(demo)
    app.run(debug=True)
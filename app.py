from flask import Flask, app, render_template, request, redirect, current_app
from flask.globals import session
from flask.helpers import flash, url_for
import cv2
import config
import datetime
from sqlalchemy import create_engine, engine
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.functions import mode, user
import settings
from more.face import face
import pymysql
pymysql.install_as_MySQLdb()      #ModuleNotFoundError: No module named ' MysQLdb'


app = Flask(__name__, 
# template_folder='templates' , static_url_path='/',static_folder='static'
)
# app.config['SECRET_KEY'] = '123'
app.secret_key = '2204'
# print(app.config)   # 查看配置文件
app.config.from_object(settings)

# 使用集成方法处理 SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/nebula?charset=utf8' # "NbiTAGtSBbVbjyNI"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)   # 实例化 db 对象
        
print(db)

# @app.before_request
# def before_request():
#     g.user = None
#     if 'user_id' in session:
#         user = [u for u in users if u.id == session['user_id']]
#         g.user = user

# @app.route("/")
# def index():
#     if face()==True:
#         return render_template('index.html')
#     else:
#         return render_template('login.html')



# @app.route("/login", methods=['GET','POST'])
# def login():
#     """
#     docstring
#     """
#     if request.method == 'GET':
#         return render_template('login.html') 
#     else:
#         request.method == 'POST'
#         username = request.form.get("username")
#         password = request.form.get("password")
#         user = [u for u in users if u.username== username]
#         if len(user)>0:
#             user = user[0]
#         if user and user.password == password:
#             session['user_id'] = user.id

#         # if username in users:
#         #     if username=='mike' and password=='4444':
#         #         session['username'] = username
#                 # return "登录成功"
#             return render_template('index.html')
#         else:
#             # return "登录失败"
#             # flash('登录失败')
#             return render_template('login.html', error = '用户名或密码错误')
#             # return '登录失败'


# # 定制 404 错误页
# @app.errorhandler(404)
# def page_not_found(e):
#     # return '网页出错了！'
#     return render_template('404.html')

# # 定制 500 错误页
# @app.errorhandler(500)
# def server_error(e):
#     # return '网页出错了！'
#     return render_template('500.html')



if __name__ == "__main__":
    from controller.index import *
    app.register_blueprint(index)
    from controller.login import *
    app.register_blueprint(loginer)
    from controller.article_modle import *
    app.register_blueprint(article)
    # from controller.my_ajax import *
    # app.register_blueprint(my_ajax)
    # from controller.nebula_api import *
    # app.register_blueprint(nebula_api)
    # from controller.article_list import *
    # app.register_blueprint(article_list)

    app.run(
        # host='0.0.0.0', port='8080',       # IP定义为 0.0.0.0 后，可外网通过IP地址访问，默认只能本机访问
        debug=True
        )      
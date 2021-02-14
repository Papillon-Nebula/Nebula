from flask import Flask, app, render_template, request, redirect
from flask.globals import session
from flask.helpers import flash, url_for
import cv2
from module.models import Users
import config
import datetime
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.functions import user
import settings
from more.face import face


app = Flask(__name__, 
# template_folder='templates' , static_url_path='/',static_folder='static'
)
# app.config['SECRET_KEY'] = '123'
app.secret_key = '123'
print(app.config)   # 查看配置文件
app.config.from_object(settings)


# @app.route("/")
# def hello():
#     return render_template('index.html')
@app.route("/")
def index():
    if face()==True:
        return render_template('Nebula.html')
    else:
        return render_template('login.html')

@app.route("/login", methods=['GET','POST'])
def login():
    """
    docstring
    """
    if request.method == 'GET':
        return render_template('login.html') 
    else:
        request.method == 'POST'
        username = request.form.get("username")
        password = request.form.get("password")
        if username=='mike' and password=='4444':
            session['username'] = username
            # return "登录成功"
            return render_template('Spyre - Slick contemporary multipurpose theme.html')
        else:
            # return "登录失败"
            # flash('登录失败')
            return render_template('login.html', error = '用户名或密码错误')
            # return '登录失败'




if __name__ == "__main__":
    app.run(
        # host='0.0.0.0', port='8080',       # IP定义为 0.0.0.0 后，可外网通过IP地址访问，默认只能本机访问
        # debug=True
        )      
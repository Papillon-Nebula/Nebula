from flask import Blueprint, request, render_template, redirect
from flask.globals import session
from sqlalchemy.sql.operators import is_precedent
from module.users import Users
from main import db
from common.utility import ImageCode
import hashlib


loginer = Blueprint('login', __name__,)

@loginer.route('/vcode')
def vcode():
    code, bstring = ImageCode()


@loginer.route('/login', methods=['POST','GET'])   # register and login
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        request.method == 'POST'
        username = request.form.get("username")
        password = request.form.get("password")
        # password = hashlib.md5(password.encode()).hexdigest()       # 哈希值化 密码
        # user = [u for u in Users if u.name==username]
        # if username == user.name and password == user.password:
        if username == 'mike' and password == '111':
            return 'sucess!'
        else:
            return 'fail!'
        # if len(user)>0:
        #     user = user[0]
        # if user and user.password == password:
        #     session['user_id'] = user.id
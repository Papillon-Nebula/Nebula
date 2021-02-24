from flask import Blueprint, request, render_template, redirect, make_response
from flask.globals import session
from sqlalchemy.sql.operators import is_precedent

from app import db
from common.utility import ImageCode, gen_email_code, send_email
import hashlib
import re


loginer = Blueprint('login', __name__,)

@loginer.route('/vcode')
def vcode():
    code, bstring = ImageCode().get_code()
    response = make_response(bstring)
    response.headers['Content-Type'] = 'image/jpeg'
    session['vcode'] = code.lower()
    return response

@loginer.route('/ecode', methods=['POST'])
def ecode():
    email = request.form.get('email')
    if not re.match('.+@.+\..+', email):
        return 'email-invalid'
    code = gen_email_code()
    print(code)
    try:
        send_email(email, code)
        session['ecode'] = code
        return 'send-pass'
    except:
        return 'send-fail'


@loginer.route('/login', methods=['POST','GET'])   # register and login
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        from module.users import Users
        user = Users()
        print(user)
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        # ecode = request.form.get('ecode').strip()
        
        # 验证用户是否已经注册
        if len(user.find_by_username(username))>0:
            print(user.find_password_by_username(username)[0])
            password = hashlib.md5(password.encode()).hexdigest()
            print(password)
            if password != user.find_password_by_username(username)[0]:
                return '该用户已经注册过了!'
            else:
                return username + '欢迎回来!'
        
        else:
            # 实现注册功能
            password = hashlib.md5(password.encode()).hexdigest()
            result = user.do_register(username, password)
            # 存用户信息
            session['islogin'] = 'true'
            # session['userid'] = result.userid
            session['username'] = username
            # session['nickname'] = result.nickename
            # session['role'] = result.role
            return 'Welcome to Nebula,' + session['username']
            # return 'user-pass!'
    else:
        return '跑偏了！'



    # else:
    #     request.method == 'POST'
    #     if 
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #     # password = hashlib.md5(password.encode()).hexdigest()       # 哈希值化 密码
    #     # user = [u for u in Users if u.name==username]
    #     # if username == user.name and password == user.password:
    #     if username == 'mike' and password == '111':
    #         return 'sucess!'
    #     else:
    #         return 'fail!'
        # if len(user)>0:
        #     user = user[0]
        # if user and user.password == password:
        #     session['user_id'] = user.id


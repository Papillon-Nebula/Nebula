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
        # return render_template('login copy.html')
        if 'islogin' not in session:
            return render_template('login.html')
        else:
            return session['username'] + "已常驻客户端"
    elif request.method == 'POST':
        username = request.data
        # print(username)
        from module.users import Users
        user = Users()
        username = request.form.get('username', None).strip()
        password = request.form.get('password', None).strip()
        print(username)
        if username == '':
            return '请输入铭牌！'
        elif len(user.find_by_username(username))>0:
            if request.form.get('password') == '':
            # print(user.find_password_by_username(username)[0])
            # password = hashlib.md5(password.encode()).hexdigest()
            # print(password)
                # html = '您即将登录'+ username
                result =  '请输入指令！'
                return result
            else:
                password = hashlib.md5(password.encode()).hexdigest()
                if password == user.find_password_by_username(username)[0]:
                    print(user.find_password_by_username(username)[0])
                    # return username + '欢迎回来!'
                     # 存用户信息
                    session['islogin'] = 'true'
                    # session['userid'] = result.userid
                    session['username'] = username
                    # session['nickname'] = result.nickename
                    # session['role'] = result.role
                    return 'Welcome to Nebula,' + session['username']
                elif password != user.find_password_by_username(username)[0]:
                    print(user.find_password_by_username(username)[0])
                    # flash('密码错误请重新登录！')
                    # return render_template('login copy.html')
                    return render_template('login.html')

        elif len(user.find_by_username(username))==0:
            if password =='':
                result = '您即将以' + username + '注册并进入星际空间！'
                return result 
            elif '.' in str(password):
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
                return '密码强度不足'
            
    else:
        return '未知事件，请留意！'



# def login_bate1():
#     if request.method == 'GET':
#         return render_template('login.html')
#     elif request.method == 'POST':
#         from module.users import Users
#         user = Users()
#         print(user)
#         username = request.form.get('username').strip()
#         password = request.form.get('password').strip()
#         # ecode = request.form.get('ecode').strip()
        
#         # 验证用户是否已经注册
#         if len(user.find_by_username(username))>0:
#             print(user.find_password_by_username(username)[0])
#             password = hashlib.md5(password.encode()).hexdigest()
#             print(password)
#             if password != user.find_password_by_username(username)[0]:
#                 return '该用户已经注册过了!'
#             else:
#                 return username + '欢迎回来!'
        
#         else:
#             # 实现注册功能
#             password = hashlib.md5(password.encode()).hexdigest()
#             result = user.do_register(username, password)
#             # 存用户信息
#             session['islogin'] = 'true'
#             # session['userid'] = result.userid
#             session['username'] = username
#             # session['nickname'] = result.nickename
#             # session['role'] = result.role
#             return 'Welcome to Nebula,' + session['username']
#             # return 'user-pass!'
#     else:
#         return '跑偏了！'

from time import time
from flask import Blueprint, request, render_template, redirect, make_response
from flask.globals import session
from flask.helpers import flash
from flask.wrappers import Response
from sqlalchemy.sql.operators import is_precedent
from werkzeug.utils import html

from app import db
from common.utility import ImageCode, gen_email_code, send_email
import hashlib
import re


my_ajax = Blueprint('my_ajax', __name__)

@my_ajax.route('/login', methods=['GET', 'POST'])
def yanzhen():
    if request.method == 'GET':
        # return render_template('login copy.html')
        if 'islogin' not in session:
            return render_template('login copy.html')
        else:
            return session['username'] + "已常驻客户端"
    elif request.method == 'POST':
        username = request.data
        # print(username)
        from module.users import Users
        user = Users()
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        print(username)
        if username == '':
            return '姓名不能为空'
        elif len(user.find_by_username(username))>0:
            if request.form.get('password') == '':
            # print(user.find_password_by_username(username)[0])
            # password = hashlib.md5(password.encode()).hexdigest()
            # print(password)
                # html = '您即将登录'+ username
                html =  '密码不能为空'
                return html
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
                    return '密码错误请重新输入'

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

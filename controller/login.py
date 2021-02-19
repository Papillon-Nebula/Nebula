from flask import Blueprint, request, render_template, redirect
from flask.globals import session
from sqlalchemy.sql.operators import is_precedent
from module.models import Users
from main import db


loginer = Blueprint('login', __name__)

@loginer.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        request.method == 'POST'
        username = request.form.get("username")
        password = request.form.get("password")
        # user = [u for u in Users if u.username== username]
        if username == 'mike' and password == '111':
            return 'sucess'
        else:
            return 'deil'
        # if len(user)>0:
        #     user = user[0]
        # if user and user.password == password:
        #     session['user_id'] = user.id
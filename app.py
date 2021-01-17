from flask import Flask, app, render_template, request, redirect
from flask.globals import session
from flask.helpers import flash, url_for
import cv2



app = Flask(__name__)
# app.config['SECRET_KEY'] = '123'
app.secret_key = '123'


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


def face():
    """
    docstring
    """
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while (True):
    # 循环捕获每一帧
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        print("发现{0} 人脸!".format(len(faces)))
        if len(faces) != 0:
            return True
        else:
            return False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按键q停止显示
            break


# 关闭
    # cap.release()
    # cv2.destroyAllWindows()

# face()


if __name__ == "__main__":
    app.run(debug=True)
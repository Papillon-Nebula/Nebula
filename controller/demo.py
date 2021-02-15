from flask import Blueprint

demo = Blueprint('demo', __name__,url_prefix='/demo')


@demo.route('/demo')
def mydemo():
    return '这是另一个模块的返回内容'
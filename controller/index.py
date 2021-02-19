from flask import Blueprint, render_template, request
from flask.json import jsonify

index = Blueprint('index', __name__,)


@index.route('/')
def home():
    return render_template('index.html')

# @index.route('/getUserID', methods=['POST'])
# def get_user_id():
#     phone = request.json.get("phoneNumber").strip()
#     if phone:
#         if not (len(phone)) == 11 and re.match(phone_re, phone)):
#             return jsonify({"code":"2001", "phoneNumber": phone, "msg":"手机号格式不正确！"})
#         else：
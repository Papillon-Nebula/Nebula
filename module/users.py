from flask.blueprints import Blueprint
from sqlalchemy import Table, MetaData
from common.database import dbconnect
import time, random
# users = Blueprint('models',__name__)

dbsession, md ,DBase = dbconnect()

class Users(DBase):
    __table__ = Table('users', md, autoload=True)

    #查询用户名，可用于注册时判断用户名是否已注册，也可用于登录校验
    def find_by_username(self, username):
        result = dbsession.query(Users).filter_by(name=username).all()
        print(result)
        return result

    
    #实现注册，直次注册时用户只需要输入用户名和密码，所以只需要两个参数
    #注册时，在模型类中为其他字段尽力生成一 -些可用的值，虽不全面，但可用
    #通常用户注册时不建议填写太多资料，影响体验，可待用户后续逐步完普
    def do_register(self, username, password):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        nickname = username.split('@')[0]       #默认将邮箱账号前缀作为呢称
        avatar = str(random.randint(1,9))      #从15张头像图片中随机选择一张
        user = Users(name=username, password=password
        # , role='user', nickname=nickname, avatar=avatar+'.jpg', createtime=now, updatetime=now
        )
        dbsession.add(user)
        dbsession.commit()
        return user

    def find_password_by_username(self, username):
        result = dbsession.query(Users.password).filter_by(name=username).first()
        return result



    # def find_by_userid(self, userid):
    #     row = dbsession.query(Users).filter_by(userid=userid).first()
    #     return row
    
    # def find_user_by_id(self, userid):
    #     row = dbsession.query(Users).filter(Users.userid == userid).first()
    #     return row

    # def find_user_by_id2(self, userid):
    #     row = Users.query.filter(Users.userid == userid).first()
    #     print(row)
    #     return row
    # def find_all_user(self):
    #     result = dbsession.query(Users).all()
    #     return result
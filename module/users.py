from sqlalchemy import Table, MetaData
from main import db

class Users(db.Model):
    __table__ = Table('users', MetaData(bind=db.engine), autoload=True)


    def find_user_by_id(self, userid):
        row = db.session.query(Users).filter(Users.userid == userid).first()
        return row
    
    def find_user_by_id2(self, userid):
        row = Users.query.filter(Users.userid == userid).first()
        print(row)
        return row
    def find_all_user(self):
        result = db.session.query(Users).all()
        return result
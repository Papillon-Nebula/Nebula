import datetime
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import user
from flask import Blueprint
models = Blueprint('models',__name__)

Base = declarative_base()

engine = create_engine(
        "mysql+pymysql://debian-sys-maint:"+    
        "qhpG5ItfL6ybaSaM"
        # "eTiRzkxyAgOtANbJ"
        "@localhost:3306/nebula?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    password = Column(String(32), nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)
    extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id','name', name='uix_id_name'),
        Index('ix_id_name','name','email')
    )

    

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


# session = sessionmaker(engine)
# session = scoped_session(session)
# ret = session.query(Users.id,Users.name).all()
# print(ret)


# session = sessionmaker(engine)
# session = scoped_session(session)

# session.query(Users).filter(Users.id==1).update({"name":"papillon-nebula"})
# ret = session.query(Users.id,Users.name).all()
# print(ret)
# session.commit()

if __name__ == "__main__":
    create_table()
    # drop_table()
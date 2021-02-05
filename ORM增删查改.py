from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
# from models import Users
from models import Users
from sqlalchemy import engine,create_engine

engine = create_engine(
    "mysql+pymysql://debian-sys-maint:"+
    # "NbiTAGtSBbVbjyNI"
    "cFELvF0gljCg4nOK"
    "@localhost:3306/nebula?charset=utf8",
    # max_overflow=0,
    # pool_size=5,
    # pool_timeout=30,
    # pool_recycle=-1
)

print(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# # Base = declarative_base()
# db_session = scoped_session(session)

# ret = db_session.query(Users).first()
# print(ret)


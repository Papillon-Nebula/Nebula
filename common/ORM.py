from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import engine,create_engine
from sqlalchemy.sql.selectable import FromClause
from controller.index import index
from common.database import dbconnect
from common.models import Users

engine = create_engine(
        "mysql+pymysql://debian-sys-maint:"+
        # "qhpG5ItfL6ybaSaM"
        "eTiRzkxyAgOtANbJ"
        "@localhost:3306/nebula?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )

# print(engine)

# Session = sessionmaker(bind=engine)
# # Base = declarative_base()
# db_session = scoped_session(session)

# ret = db_session.query(Users).first()
# print(ret)

session = sessionmaker(engine)
session = scoped_session(session)

session.query(Users).filter(Users.id==1).update({"name":"papillon-nebula"})
ret = session.query(Users.id,Users.name).all()
print(ret)
session.commit()
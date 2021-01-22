import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)
    extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id','name', name='uix_id_name'),
        Index('ix_id_name','name','email')
    )

def create_table():
    engine = create_engine(
        "mysql+pymysql://debian-sys-maint:"+
        # "NbiTAGtSBbVbjyNI"
        "cFELvF0gljCg4nOK"
        "@localhost:3306/nebula?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )
    Base.metadata.create_all(engine)


def drop_table():
    engine = create_engine(
        "mysql+pymysql://debian-sys-maint:"+
        # "NbiTAGtSBbVbjyNI"
        "cFELvF0gljCg4nOK"
        "@localhost:3306/nebula?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )
    Base.metadata.drop_all(engine)

if __name__ == "__main__":
    # create_table()
    drop_table()
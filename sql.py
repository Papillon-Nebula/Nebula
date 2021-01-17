import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.engine.base import Engine


engine = create_engine(
    "mysql+pymysql://debian-sys-maint:NbiTAGtSBbVbjyNI@1.203.144.58:3306/test?charset=utf8",
    max_overflow=0,
    pool_size=5,
    pool_timeout=30,
    pool_recycle=-1
)

conn=engine.row_connection()

cursor = conn.cursor()

cursor.excute('select * from ')
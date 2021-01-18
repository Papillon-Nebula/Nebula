import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
# from sqlalchemy import engine
from sqlalchemy.engine.base import Engine


engine = create_engine(
    "mysql+pymysql://debian-sys-maint:NbiTAGtSBbVbjyNI@127.0.0.1:3306/nebula?charset=utf8",
    max_overflow=0,
    pool_size=5,
    pool_timeout=30,
    pool_recycle=-1
)

conn=engine.raw_connection()

cursor = conn.cursor()

cursor.execute('select * from Nebula')
res = cursor.fetchall()
print(res)
import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
# from sqlalchemy import engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

def ret():
    engine = create_engine(
        "mysql+pymysql://debian-sys-maint:"+
        # "NbiTAGtSBbVbjyNI"
        "eTiRzkxyAgOtANbJ"
        "@localhost:3306/nebula?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )

    conn=engine.raw_connection()

    cursor = conn.cursor()

    cursor.execute('select * from members')
    ret = cursor.fetchall()
    print(ret)
    ret = list(ret)
    return ret

ret()
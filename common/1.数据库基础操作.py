from distutils.util import execute
import time
import pymysql
import threading
from pymysql.charset import Charset
from pymysql.cursors import DictCursor
import sqlalchemy
from sqlalchemy import create_engine
# from sqlalchemy import engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

"""
所有的I/O操作：文件，数据库，网络等，均有以下三个基本步骤
第一步：连接到MySQL数据库
第二步：执行SQL语句
1、实例化一个游标对象； 2、定义SQL语句； 3、通过游标执行； 4、处理执行结果；
第三步：关闭数据库连接
"""

# 第一步：连接到MySQL数据库
conn = pymysql.connect(host = 'localhost',port = 3306, user = 'debian-sys-maint', password = 'eTiRzkxyAgOtANbJ', charset = 'utf8', database = 'nebula', autocommit = True)
# 第二步：执行SQL语句
# 1、实例化一个游标对象； 2、定义SQL语句； 3、通过游标执行； 4、处理执行结果；
cursor = conn.cursor()
sql = "select * from users"
cursor.execute(sql)
result = cursor.fetchall()
# print(result)

"""
一般情况下，不建议使用下标来获取列的值，如下，表结构发生改变时，查询的内容会存在异常
for row in result:
    print(row[2])
建议使 Key-Value 来获取数据（Key==》列名， Value==》单元格的值），如下示例
代码可读性更强，代码维护更高效
建议面对一些复杂的SQL，先在Navicat 调试完成后再整合到代码中
"""
cursor = conn.cursor(DictCursor)
# 1. 查询
sql = "select * from users"
cursor.execute(sql)
result = cursor.fetchall()
# print(result)
# print(result[1]['name'])


# 2. 更新
sql = "update users set name='mik18' where id=2"
cursor.execute(sql)
# conn.commit()   提交修改：update ； insert ， delete
print(execute)

# print(result[1]['name'])
# 第三步：关闭数据库连接
cursor.close()
conn.close()


print(conn.get_server_info())


# def ret():
#     engine = create_engine(
#         "mysql+pymysql://debian-sys-maint:"+
#         # "NbiTAGtSBbVbjyNI"
#         "eTiRzkxyAgOtANbJ"
#         "@localhost:3306/nebula?charset=utf8",
#         max_overflow=0,
#         pool_size=5,
#         pool_timeout=30,
#         pool_recycle=-1
#     )

#     conn=engine.raw_connection()

#     cursor = conn.cursor()

#     cursor.execute('select * from members')
#     ret = cursor.fetchall()
#     print(ret)
#     ret = list(ret)
#     return ret

# ret()
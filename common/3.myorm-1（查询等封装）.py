import pymysql
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
class MySQL:
    def __init__(self) -> None:
        # 实例化即创建与数据库之间的连接
        # 第一步：连接到MySQL数据库
        conn = pymysql.connect(host = 'localhost',port = 3306, user = 'debian-sys-maint', password = 'qhpG5ItfL6ybaSaM', charset = 'utf8', database = 'nebula', autocommit = True)
        self.cursor = conn.cursor(DictCursor)
        
    # 封装基础查询语句
        # 第二步：执行SQL语句
        # 1、实例化一个游标对象； 2、定义SQL语句； 3、通过游标执行； 4、处理执行结果；
    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    # 执行修改操作
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            return 'OK'
        except:
            return 'Fail'


class Users:
    table_name = 'users'

    # 构造方法，传递字典参数作为 Insert 的 Key 和 Value
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        print(self.__dict__)


    # 封装查询操作
    def select(self, **where):
        # sql = "select * from %s where %s " % (self.table_name, where)
        sql = "select * from %s" % self.table_name
        if where is not None:
            sql += " where"
            for k, v in where.items():
                sql += " %s = '%s' and" % (k, v) 
            sql += ' 1=1'
        print(sql)
        result = MySQL().query(sql)
        return result



    # 封装新增: insert into table(c1, c2, c3) values(v1, v2, v3)
    def insert(self):
        keys = []
        values = []
        for k, v in self.__dict__.items():
            keys.append(k)
            values.append(str(v))

        sql = "insert into %s(%s) values('%s')" % (self.table_name, ",".join(keys), "','".join(values))
        print(sql)
        result = MySQL().execute(sql)
        print(result)


if __name__ == '__main__':
    # db = MySQL()
    # result = db.query('select * from users')
    # print(result)

    # user = Users()
    # result = user.select("id=1")    配合45行使用，使用时注释掉46行及以下内容
    # result = user.select(id = 1, name = 'mike')
    # result0 = user.select()
    # print(result)
    # print(result0)
    user = Users(name = 'mike2', email = 'papillon', extra = 'qq:1057324546')
    user.insert()
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
        conn = pymysql.connect(host = 'localhost',port = 3306, user = 'debian-sys-maint', password = 'eTiRzkxyAgOtANbJ', charset = 'utf8', database = 'nebula', autocommit = True)
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

# 封装成标准的模型类，供子类继承
# 增加 field() 方法来指定查询哪些列， * 代表所有列
class Model:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            print(self.__dict__)

    # 通过链式操作指定查询哪些类
    def field(self, columns):
        self.columns = columns    # 动态增加类实例属性
        return self

    # 带列名的查询条件：
    def select(self, **where):
        table = self.__class__.__getattribute__(self, 'table_name')
        
        if hasattr(self, 'columns'):
            sql = "select %s from %s" % (self.columns, table)
        else:
            sql = "select * from %s" % table

        if where is not None:
            sql += " where"
            for k, v in where.items():
                sql += " %s = '%s' and" % (k, v) 
            sql += ' 1=1'
        print(sql)
        result = MySQL().query(sql)
        return result
        

    # 正常新增数据
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



# 定义子类 Users 和 Article   
class Users(Model):
    table_name = 'users'

    # 调用父类的构造方法
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Article(Model):
    table_name = 'article'

    # 调用父类的构造方法
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


user = Users()
article = Article()
# result = user.select(email = 'papillon')    
result0 = user.field('name, email').select(email = 'papillon')
print(result0)

# result1 = article.select(articleid = 1)
# print(result1)

if __name__ == '__main__':
    pass
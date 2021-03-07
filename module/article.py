# from sqlalchemy.ext.declarative.api import declarative_base
# from sqlalchemy.orm import scoped_session
# from sqlalchemy.orm.session import sessionmaker
# from sqlalchemy import engine, create_engine
# from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
# import datetime
# from sqlalchemy.sql.expression import column
# from sqlalchemy.sql.schema import Column
# from sqlalchemy.sql.type_api import INTEGERTYPE

# engine = create_engine("mysql+pymysql://debian-sys-maint:eTiRzkxyAgOtANbJ@localhost:3306/nebula?charset=utf8", echo=True)

# Base = declarative_base()
# session = sessionmaker(engine)
# session = scoped_session(session)
from flask.blueprints import Blueprint
from sqlalchemy import Table, MetaData
from common.database import dbconnect
import time, random

dbsession, md ,DBase = dbconnect()


class Article(DBase):
    __table__ = Table('article', md, autoload=True)
    # id = Column(Integer, primary_key=True)
    # title = Column(String(32), index=True, nullable=False)
    # author = Column(String(32), index=True, nullable=False)
    # keywords = Column(String(32), index=True, nullable=False)
    # description = Column(String(32), index=True, nullable=False)
    
    # name = Column(String(32), index=True, nullable=False)
    # email = Column(String(32), unique=True)
    # password = Column(String(32), nullable=False)
    # ctime = Column(DateTime, default=datetime.datetime.now)
    # extra = Column(Text, nullable=True)
    # __table_args__ = (
    #     UniqueConstraint('id','name', name='uix_id_name'),
    #     Index('ix_id_name','name','email')
    # )


    def find_article_by_id(id):
        # ret = dbsession.query(Article).first()
        ret = dbsession.query(Article).filter(Article.id == id).first()
        return ret

    def find_all(start,count):
        # ret = dbsession.query(Article).first()
        ret = dbsession.query(Article).order_by(Article.id.asc()).limit(count).offset(start).all()
        return ret

    def find_5(start,count):
        # ret = dbsession.query(Article).first()
        count = count
        ret = dbsession.query(Article.id, Article.title).order_by(Article.id.asc()).limit(count).offset(start).all()
        
        return ret



# class Article(DBase):
#     __tablename__ = Table('cms_articlecontent', md, autoload=True)
    # articleId = Column(Integer, primary_key=True)
    # # articleId = Column(Integer, ForeignKey('cms_article.id'))
    # content = Column(String(32), index=True)
    

# ret = dbsession.query(Cms_Article, Article).join(Article, Article.articleId==Cms_Article.id).limit(10).all()

    # def __repr__(self) -> str:
    #     return super().__repr__()

# ret = session.query(Cms_Article.id, Cms_Article.title, Article.content, Cms_Article.author,Cms_Article.description, Cms_Article.keywords).filter(Cms_Article.id ==396026).first()

# ret = session.query(Cms_Article.id,Cms_Article.title, Article.content).join(Article, Article.articleId==Cms_Article.id).filter(Cms_Article.id == 332542).first()

# for Cms_Article, Article in ret:
#     print(Cms_Article.id,Cms_Article.title,Cms_Article.author,Article.content)


# print(ret)
# print(ret.__dict__.items())



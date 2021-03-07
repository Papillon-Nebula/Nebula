from module.article import Article
from flask.templating import render_template
from common.database import dbconnect
from flask import Blueprint, jsonify
from flask.globals import session
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from app import db
# from module.ebrun import Article,Cms_Article

nebula_api = Blueprint('nebula_api', __name__)

dbsession, md ,DBase = dbconnect()


@nebula_api.route('/api/article', methods=['GET', 'POST'])
def article_api():
    result = Article.find_all(1,1)
    return render_template('article.html',result=result)
    
@nebula_api.route('/article_recommend', methods=['GET', 'POST'])
def article_recommend():
    result = Article.find_5(15,15)
    return jsonify(result)
    # return render_template('article.html',result=result)
        
    # ret = dbsession.query(Cms_Article, Article).join(Article, Article.articleId==Cms_Article.id).limit(10).all()
    # article_list = []
    # article = {}
    # article_list.append()
    # for Cms_Article, Article in ret:
    #     article['article_id'] = Cms_Article.id
    #     article['article_title'] = Cms_Article.title
    #     article['article_author'] = Cms_Article.author
    #     article['article_content'] = Article.content
    #     print(Cms_Article.id,Cms_Article.title,Cms_Article.author,Article.content)

    # print(article_list)
    # return article_list
    # return jsonify()

# article_api()
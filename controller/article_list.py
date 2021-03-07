from flask import Blueprint
from flask.templating import render_template
from module import article
from module.article import *
article_list = Blueprint('article_list', __name__)

@article_list.route('/article_list')
def article_List():
    Article_list =  Article.find_all(10,10)
    print(Article_list)
    return render_template('article_list.html', result=Article_list)
    # result = Article_list

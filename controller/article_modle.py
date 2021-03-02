from flask import Blueprint
from flask import render_template

article = Blueprint('article',__name__)


@article.route('/article/<int:article_id>')
def article_read(article_id):
    from module.ebrun import Cms_Article
    result = Cms_Article.article()
    print(type(result))
    list = []

    for row in result:
        dict = {}
        for k,v in row.__dict__.item():
            if not k.startswith('_sa_instance_state'):

                dict[k] = v
            
    # print(list)
    # return render_template('article-model.html', result=list)

    return str(list)


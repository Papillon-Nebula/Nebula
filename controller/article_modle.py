from flask import Blueprint
from flask import render_template
from flask.json import jsonify

article = Blueprint('article',__name__)


@article.route('/article/<int:article_id>')
def article_read(article_id):
    from module.article import Article
    result = Article.find_article_by_id(article_id)
    print(type(result))
    # print(result.__dict__)

    list = []
    dict = {}
    for k,v in result.__dict__.items():
        if not k.startswith('_sa_instance_state'):
            dict[k] = v
    list.append(dict)
    print(article_id)
            
    print(list)
    # return render_template('article-model.html', result=list)

    return jsonify(list)


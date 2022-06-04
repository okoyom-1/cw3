from flask import Blueprint, render_template, request
from utils import search_for_posts, find_posts_by_tag

search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route('/search/')
def search_page():
    if request.args.get('s'):
        return render_template('search.html', posts=search_for_posts(request.args.get('s')))
    else:
        return render_template('search.html')


@search_blueprint.route('/tag/')
def tag_page():
    return render_template('search.html', posts=find_posts_by_tag(request.args.get('tag')))

from flask import Blueprint, render_template
from utils import get_post_all, count_bookmarks

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def index_page():
    return render_template('index.html', posts=get_post_all(), bookmarks_count=count_bookmarks())

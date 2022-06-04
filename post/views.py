from flask import Blueprint, render_template
from utils import get_comments_by_post_id, get_post_by_pk

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/post/<int:pid>')
def posts_page(pid):
    return render_template('post.html', comments=get_comments_by_post_id(pid), post=get_post_by_pk(pid))

from flask import Blueprint, render_template
from utils import get_post_by_user

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/user/<username>')
def user_page(username):
    return render_template('user-feed.html', posts=get_post_by_user(username),
                           user=get_post_by_user(username)[0]['poster_name'])

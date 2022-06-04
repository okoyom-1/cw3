from flask import Blueprint, render_template, request, redirect
from utils import get_post_by_pk, add_bookmark, get_bookmarks, delete_bookmark

bookmark_blueprint = Blueprint('bookmark_blueprint', __name__)


@bookmark_blueprint.route('/bookmarks/')
def bookmarks_page():
    posts = [get_post_by_pk(bookmark.get('pk')) for bookmark in get_bookmarks()]
    return render_template('bookmarks.html', posts=posts)


@bookmark_blueprint.route('/bookmarks/add/', methods=['POST'])
def bookmark_add():
    add_bookmark(int(request.form.get('post_id')))
    return redirect('/', code=302)


@bookmark_blueprint.route('/bookmarks/remove/<int:post_id>')
def bookmark_remove(post_id):
    delete_bookmark(post_id)
    return redirect('/bookmarks/', code=302)

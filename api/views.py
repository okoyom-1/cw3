from flask import Blueprint, jsonify
from utils import get_post_all, get_post_by_pk
import logging

api_blueprint = Blueprint('api_blueprint', __name__)
api_logger = logging.getLogger('api_log')


@api_blueprint.route('/api/posts/')
def api_get_posts():
    api_logger.info("Получение списка всех постов")
    return jsonify(get_post_all())


@api_blueprint.route('/api/posts/<int:post_id>')
def api_get_post_by_id(post_id):
    api_logger.info(f"Получение поста с номером {post_id}")
    return jsonify(get_post_by_pk(post_id))

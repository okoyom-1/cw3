from flask import Flask
from main.views import main_blueprint
from search.views import search_blueprint
from post.views import post_blueprint
from bookmark.views import bookmark_blueprint
from user.views import user_blueprint
from api.views import api_blueprint
import logging


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(bookmark_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)

app_logger = logging.getLogger('api_log')
app_logger.setLevel(logging.INFO)

app_handler = logging.FileHandler(filename='./api.log', encoding='utf-8')
app_handler.setLevel(logging.INFO)

log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

app_handler.setFormatter(log_format)

app_logger.addHandler(app_handler)


@app.errorhandler(404)
def not_found_page(error):
    return f"Старница не найдена:<br>{error}"


@app.errorhandler(500)
def server_error_page(error):
    return f"Серверная ошибка:<br>{error}"


if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify
import logging

from app.main.views import *

app = Flask(__name__)
print(app.config)

app.config["JSON_AS_ASCII"] = False

# регистрация блюпринтов
app.register_blueprint(main_page_blueprint)
app.register_blueprint(post_page_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_posts_blueprint)
app.register_blueprint(tag_page_blueprint)
app.register_blueprint(add_bookmark_blueprint)
app.register_blueprint(load_bookmarks_blueprint)
app.register_blueprint(delete_bookmark_blueprint)

# объявление файла для хранения логов
logfile = "api.log"

# создание логгера для хранения логов
log = logging.getLogger("api_logs")

# объявление уровня события для логирования
log.setLevel(logging.INFO)

# объявление направления вывода логов - в файл (создание обработчика)
filehandler = logging.FileHandler(logfile)

# форматирование вывода логов в файл
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# присвоение хендлеру формата вывода логов
filehandler.setFormatter(formatter)

# добавляем обработчик
log.addHandler(filehandler)




@app.errorhandler(404)
def page_not_found(error):
    """ обработка ошибки 404(несуществующая страница)"""
    return f"<h1>404:Такая страница не найдена</h1>", 404


@app.errorhandler(500)
def internal_server_error(error):
    """ обработка ошибки 500(ошибка на стороне сервера)"""
    return f"<h1>500:Ошибка сервера</h1>", 500


@app.route("/api/posts", methods=["GET"])
def read_posts():
    """ обработка API-запроса всех постов, логирование запроса"""
    posts = get_all_posts()
    log.info("Запрос /api/posts")
    return jsonify(posts)


@app.route("/api/posts/<int:pk>", methods=["GET"])
def read_post(pk):
    """ обработка API-запроса поста по id, логирование запроса"""
    post = get_post_by_pk(pk)
    log.info(f"Запрос /api/posts/{pk}")
    return jsonify(post)


if __name__ == "__main__":
    app.run()

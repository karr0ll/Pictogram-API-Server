from flask import Blueprint, redirect, render_template

from bookmarks.dao.bookmarks_dao import BookmarksDAO

bookmarks_dao = BookmarksDAO()

add_bookmark_blueprint = Blueprint('add_bookmark_blueprint', __name__, template_folder="templates")
load_bookmarks_blueprint = Blueprint('load_bookmarks_blueprint', __name__, template_folder="templates")
delete_bookmark_blueprint = Blueprint('delete_bookmark_blueprint', __name__, template_folder="templates")

@add_bookmark_blueprint.route("/bookmarks/add/<int:post_id>", methods=["GET"])
def create_bookmark(post_id):
    bookmarks_dao.add_bookmark(post_id)
    return redirect("/", code=302)


@load_bookmarks_blueprint.route("/bookmarks/")
def load_all_bookmarks():
    """ загружает все посты в закладках """
    posts = bookmarks_dao.load_from_json()
    return render_template("bookmarks.html", posts=posts)


@delete_bookmark_blueprint.route("/bookmarks/remove/<int:post_id>")
def delete_bookmark(post_id):
    """ удаляет пост из закладок """
    bookmarks_dao.delete_by_post_id(post_id)
    return redirect("/", code=302)

from flask import render_template, Blueprint

from bookmarks.dao.bookmarks_dao import BookmarksDAO
from main_page.dao.main_dao import MainDAO

main_page_blueprint = Blueprint('main_page', __name__, template_folder="templates")
main_dao = MainDAO()
bookmarks_dao = BookmarksDAO()


@main_page_blueprint.route('/')
def page_index():
    """ отображает все посты """
    posts = main_dao.get_all_posts()
    bookmarks_counter = len(bookmarks_dao.load_from_json())
    return render_template("index.html", posts=posts, bookmarks_counter=bookmarks_counter)

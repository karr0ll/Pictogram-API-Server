from flask import Blueprint, render_template, request, redirect
from app.utils import *

main_page_blueprint = Blueprint('main_page', __name__, template_folder="templates")
post_page_blueprint = Blueprint('post_page', __name__, template_folder="templates")
search_blueprint = Blueprint('search', __name__, template_folder="templates")
user_posts_blueprint = Blueprint('user_posts', __name__, template_folder="templates")
tag_page_blueprint = Blueprint('search_posts_by_tag', __name__, template_folder="templates")
add_bookmark_blueprint = Blueprint('add_bookmark_blueprint', __name__, template_folder="templates")
load_bookmarks_blueprint = Blueprint('load_bookmarks_blueprint', __name__, template_folder="templates")
delete_bookmark_blueprint = Blueprint('delete_bookmark_blueprint', __name__, template_folder="templates")


@main_page_blueprint.route('/')
def page_index():
    """ отображает все посты """
    posts = get_all_posts()
    bookmarks_counter = len(load_bookmarks_from_json())
    return render_template("index.html", posts=posts, bookmarks_counter=bookmarks_counter)


@post_page_blueprint.route("/posts/<int:post_id>/")
def load_post(post_id):
    """ отображает все посты по их pk """
    comments = get_comments_by_post_id(post_id)
    comments_count = len(comments)
    post = get_post_by_pk(post_id)
    return render_template("post.html", comments=comments, comments_count=comments_count,
                           post=post)


@search_blueprint.route("/search/")
def search_post():
    """ отображает все посты по условию поиска """
    s = request.args.get("s")
    posts = search_for_posts(s)
    posts_found = len(posts)
    return render_template("search.html", posts=posts, posts_found=posts_found)


@user_posts_blueprint.route("/user/<user_name>")
def load_user_posts(user_name):
    """ отображает все посты пользователя"""
    posts = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts)


@tag_page_blueprint.route("/tag/<tag>")
def load_tag_page(tag):
    """ отображает все посты с заданным тегом"""
    posts = get_all_posts()
    tag_name = tag
    return render_template("tag.html", posts=posts, tag_name=tag_name)


@add_bookmark_blueprint.route("/bookmarks/add/<int:post_id>", methods=["GET"])
def create_bookmark(post_id):
    add_bookmark(post_id)
    return redirect("/", code=302)


@load_bookmarks_blueprint.route("/bookmarks/")
def load_all_bookmarks():
    """ загружает все посты в закладках """
    posts = load_bookmarks_from_json()
    return render_template("bookmarks.html", posts=posts)


@delete_bookmark_blueprint.route("/bookmarks/remove/<int:post_id>")
def delete_bookmark(post_id):
    """ удаляет пост из закладок """
    delete_bookmark_by_post_id(post_id)
    return redirect("/", code=302)

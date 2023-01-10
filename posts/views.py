from flask import Blueprint, render_template, request

from comments.dao.comments_dao import CommentsDAO
from posts.dao.posts_dao import PostsDAO

post_page_blueprint = Blueprint('post_page', __name__, template_folder="templates")
search_blueprint = Blueprint('search', __name__, template_folder="templates")
user_posts_blueprint = Blueprint('user_posts', __name__, template_folder="templates")


comments_dao = CommentsDAO()
posts_dao = PostsDAO()

@post_page_blueprint.route("/posts/<int:post_id>/")
def load_post(post_id):
    """ отображает все посты по их pk """
    comments = comments_dao.get_by_post_id(post_id)
    comments_count = len(comments)
    post = posts_dao.get_by_pk(post_id)
    return render_template("post.html", comments=comments, comments_count=comments_count,
                           post=post)


@user_posts_blueprint.route("/user/<user_name>")
def load_user_posts(user_name):
    """ отображает все посты пользователя"""
    posts = posts_dao.get_by_username(user_name)
    return render_template("user-feed.html", posts=posts)


@search_blueprint.route("/search/")
def search_post():
    """ отображает все посты по условию поиска """
    s = request.args.get("s")
    posts = posts_dao.search_for_posts(s)
    posts_found = len(posts)
    return render_template("search.html", posts=posts, posts_found=posts_found)
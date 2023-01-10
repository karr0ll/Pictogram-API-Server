import pytest

from app.utils import *


def test_get_all_posts():
    posts = get_all_posts()
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}
    for i in range(0, len(posts)):

        assert type(posts) == list, "json файл содержит не список"
        assert len(posts) > 0, "список постов пустой"
        assert posts[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


@pytest.mark.parametrize("user_name", ("leo", "johnny"))
def test_get_posts_by_user(user_name):
    posts = get_posts_by_user(user_name)
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}
    for i in range(0, len(posts)):

        assert posts[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


@pytest.mark.parametrize("post_id", (1, 2, 3))
def test_get_comments_by_post_id(post_id):
    data = get_comments_by_post_id(post_id)
    expected_keys = {"post_id", "commenter_name", "comment", "pk"}
    for i in range(0, len(data)):

        assert type(data) == list
        assert data[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


@pytest.mark.parametrize("s", ("кот", "так", "йцукен"))
def test_search_for_posts(s):
    posts = search_for_posts(s)

    try:
        assert s in posts[3]["content"]
    except:
        raise IndexError(f"искомое слово '{s}' не найдено")


def test_get_post_by_pk():
    post = get_post_by_pk(1)
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}

    assert post.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


def test_load_bookmarks_from_json():
    bookmarks = load_bookmarks_from_json()
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    for i in range(0, len(bookmarks)):

        assert type(bookmarks) == list, "json файл содержит не список"
        assert len(bookmarks) > 0, "список постов пустой"
        assert bookmarks[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


@pytest.mark.parametrize("post_id", (1, 2, 3))
def test_add_bookmark(post_id):
    bookmark = add_bookmark(post_id)
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}

    assert type(bookmark) == dict, "json файл содержит не список"
    assert bookmark.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


@pytest.mark.parametrize("post_id", (1, 2, 3))
def test_delete_bookmark(post_id):
    bookmark = add_bookmark(post_id)
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}

    assert type(bookmark) == dict, "json файл содержит не список"
    assert bookmark.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

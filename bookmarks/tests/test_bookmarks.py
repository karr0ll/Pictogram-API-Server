import pytest

from bookmarks.dao.bookmarks_dao import BookmarksDAO


@pytest.fixture()
def bookmarks_dao():
    bookmarks_dao = BookmarksDAO()
    return bookmarks_dao

class TestBookmarks:

    def test_load_from_json(self, bookmarks_dao):
        bookmarks = bookmarks_dao.load_from_json()
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

        for i in range(0, len(bookmarks)):

            assert type(bookmarks) == list, "json файл содержит не список"
            assert len(bookmarks) > 0, "список постов пустой"
            assert bookmarks[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


    @pytest.mark.parametrize("post_id", (1, 2, 3))
    def test_add_bookmark(self, post_id, bookmarks_dao):
        bookmark = bookmarks_dao.add_bookmark(post_id)
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}

        assert type(bookmark) == dict, "json файл содержит не список"
        assert bookmark.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"


    @pytest.mark.parametrize("post_id", (1, 2, 3))
    def test_delete_bookmark(self, post_id, bookmarks_dao):
        bookmark = bookmarks_dao.add_bookmark(post_id)
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                     "likes_count", "pk"}

        assert type(bookmark) == dict, "json файл содержит не список"
        assert bookmark.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

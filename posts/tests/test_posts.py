import pytest

from posts.dao.posts_dao import PostsDAO


@pytest.fixture()
def posts_dao():
    posts_dao = PostsDAO()
    return posts_dao


class TestPostsDao:

    @pytest.mark.parametrize("user_name", ("leo", "johnny"))
    def test_get_by_username(self, user_name, posts_dao):
        posts = posts_dao.load_data()
        posts_len = len(posts)
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                         "likes_count", "pk"}
        for i in range(0, posts_len):
            assert posts[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

    @pytest.mark.parametrize("s", ("кот", "так", "йцукен"))
    def test_search_for_posts(self, s, posts_dao):
        posts = posts_dao.search_for_posts(s)

        try:
            assert s in posts[3]["content"]
        except:
            raise IndexError(f"искомое слово '{s}' не найдено")

    @pytest.mark.parametrize("pk", (1, 2, 3))
    def test_get_post_by_pk(self, pk, posts_dao):
        post = posts_dao.get_by_pk(pk)
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                         "likes_count", "pk"}

        assert post.keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

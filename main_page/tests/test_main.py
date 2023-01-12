import pytest

from main_page.dao.main_dao import MainDAO


@pytest.fixture()
def main_dao():
    main_dao = MainDAO()
    return main_dao


class TestMain:

    def test_get_all_posts(self, main_dao):

        """ тестрирования загрузки всех постов для главной страницы"""

        posts = main_dao.get_all_posts()
        expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                         "likes_count", "pk"}
        for i in range(0, len(posts)):
            assert type(posts) == list, "json файл содержит не список"
            assert len(posts) > 0, "список постов пустой"
            assert posts[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

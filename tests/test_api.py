import json

from run import app
from tests.conftest import test_client


class TestAPI:

    def test_all_posts_api(self, test_client):
        response = test_client.get('/api/posts')
        data = {"poster_name", "poster_avatar", "pic", "content", "views_count",
            "likes_count", "pk"}

        for item in response.json:

            assert response.status_code == 200, "Запрошенный адрес не возвращает код 200"
            assert len(response.json) > 0, "json-файл пустой"
            assert item.keys() == data, "Ключи в файле отличаются от ожидаемых"


    def test_one_post_api(self, test_client):
        response = test_client.get('/api/posts/1')
        data = {"poster_name", "poster_avatar", "pic", "content", "views_count",
            "likes_count", "pk"}

        assert response.status_code == 200, "Запрошенный адрес не возвращает код 200"
        assert len(response.json) > 0, "json-файл пустой"
        assert response.json.keys() == data, "Ключи в файле отличаются от ожидаемых"



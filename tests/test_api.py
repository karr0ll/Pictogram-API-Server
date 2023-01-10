import json

from run import app


def test_app_all_posts_api():
    response = app.test_client().get('/api/posts')
    data = {"poster_name", "poster_avatar", "pic", "content", "views_count",
            "likes_count", "pk"}

    for item in response.json:

        assert response.status_code == 200, "Запрошенный адрес не возвращает код 200"
        assert len(response.json) > 0, "json-файл пустой"
        assert item.keys() == data, "Ключи в файле отличаются от ожидаемых"


def test_app_one_post_apy():
    response = app.test_client().get('/api/posts/1')
    data = {"poster_name", "poster_avatar", "pic", "content", "views_count",
            "likes_count", "pk"}

    assert response.status_code == 200, "Запрошенный адрес не возвращает код 200"
    assert len(response.json) > 0, "json-файл пустой"
    assert response.json.keys() == data, "Ключи в файле отличаются от ожидаемых"



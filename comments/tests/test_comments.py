import pytest

from comments.dao.comments_dao import CommentsDAO


@pytest.fixture()
def comments_dao():
    comments_dao = CommentsDAO()
    return comments_dao


class TestComments:

    @pytest.mark.parametrize("post_id", (1, 2, 3))
    def test_get_comments_by_post_id(self, post_id, comments_dao):
        data = comments_dao.get_by_post_id(post_id)
        expected_keys = {"post_id", "commenter_name", "comment", "pk"}
        for i in range(0, len(data)):
            assert type(data) == list
            assert data[i].keys() == expected_keys, "ключи в файле не соответствуют ожидаемым"

import json
import os


class CommentsDAO:

    def __init__(self, post_id=None):
        self.post_id = post_id

    def load_data(self):
        """
        загружает все посты из файла в в формате list
        """
        with open(os.path.join("data", "comments.json"), "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts

    def get_by_post_id(self, post_id):
        """
        загружает комментарии пользователей к посту
        """
        posts = self.load_data()
        comments = []
        for comment in posts:
            if comment["post_id"] == post_id:
                comments.append(comment)
        return comments

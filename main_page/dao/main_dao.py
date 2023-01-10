import json
import os


class MainDAO:

    def get_all_posts(self):
        """
        возвращает все посты
        """
        with open(os.path.join("data", "posts.json"), "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts

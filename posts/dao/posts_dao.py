import json
import os


class PostsDAO:

    def load_data(self):
        with open(os.path.join("data", "posts.json"), "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts

    def get_by_username(self, user_name):
        """
        загружает все посты пользователя
        """
        posts = self.load_data()
        user_posts = []
        for post in posts:
            if user_name.lower() == post["poster_name"]:
                user_posts.append(post)
        return user_posts

    def search_for_posts(self, s):
        """
        ищет все посты с вхождением слова из поискового запроса
        """
        posts = self.load_data()
        search_result = []
        for post in posts:
            if s.lower() in post["content"].lower():
                search_result.append(post)
        return search_result

    def get_by_pk(self, post_id):
        """
        загружает пост по его номеру pk
        """
        posts = self.load_data()
        for post in posts:
            if post_id == post["pk"]:
                return post
        else:
            raise ValueError("Такого поста нет")

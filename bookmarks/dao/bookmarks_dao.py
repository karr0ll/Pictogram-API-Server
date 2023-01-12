import json
import os


class BookmarksDAO:

    def __init__(self, post_id=None):
        self.post_id = post_id

    def load_data(self):
        with open(os.path.join("data", "posts.json"), "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts

    def get_by_pk(self, post_id):
        """
        загружает пост по его номеру pk
        """
        posts = self.load_data()
        for post in posts:
            if post_id == post["pk"]:
                return post

    def load_from_json(self):
        """
        Загружает все закладки из файла json
        """
        with open(os.path.join("data", "bookmarks.json"), "r", encoding="utf-8") as file:
            bookmarks = json.load(file)
            return bookmarks

    def add_bookmark(self, post_id):
        """
        Записывает новую закладку в файл
        """
        bookmarks = self.load_from_json()
        post = self.get_by_pk(post_id)
        if post not in bookmarks:
            bookmarks.append(post)
        with open(os.path.join("data", "bookmarks.json"), "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)
        return post

    def delete_by_post_id(self, post_id):

        """Удаляет закладку с указанным pk из файла"""

        bookmarks = self.load_from_json()
        for bookmark in bookmarks:
            if bookmark["pk"] == post_id:
                bookmarks.remove(bookmark)
        with open(os.path.join("data", "bookmarks.json"), "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)
        return bookmarks

import json
import os


def get_all_posts():
    """
    возвращает все посты
    """
    with open(os.path.join("data", "posts.json"), "r", encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def get_posts_by_user(user_name):
    """
    загружает все посты пользователя
    """
    posts = get_all_posts()
    user_posts = []
    for post in posts:
        if user_name.lower() == post["poster_name"]:
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(post_id):  # разобраться с ошибкой
    """
    загружает комментарии пользователей к посту
    """
    with open(os.path.join("data", "comments.json"), "r", encoding="utf-8") as file:
        posts = json.load(file)
        comments = []
        for comment in posts:
            if int(post_id) == comment["post_id"]:
                comments.append(comment)
        return comments


def search_for_posts(s):
    """
    ищет все посты с вхождением слова из поискового запроса
    """
    posts = get_all_posts()
    search_result = []
    for post in posts:
        if s.lower() in post["content"].lower():
            search_result.append(post)
    return search_result


def get_post_by_pk(pk):
    """
    загружает пост по его номеру pk
    """
    posts = get_all_posts()
    for post in posts:
            if pk == post["pk"]:
                return post
    else:
        raise ValueError("Такого поста нет")

def get_post_content():
    post_content = []
    posts = get_all_posts()
    for post in posts:
        post_content.append(post["content"])
    return post_content

def get_tagged_words():
    """
    ищет и выводит теги из поста
    """
    post_content = get_post_content() # получает все посты
    tags_dict = {}
    for post in post_content: # получает доступ к каждому посту
        separate_words = post.lower().split() # разбирает пост на слова
        for word in separate_words: # получает доступ к каждому слову
            if "#" in word: # ищет слово начинающееся с #
                tags_dict.update({word: f"<a href='/tag/{word}'>#{word}</a>"}) # добваляет теги в словарь для последующего сравнения
    return tags_dict


def make_tag_link():
    post_content = get_all_posts() # <class 'list'>
    tagged_words = get_tagged_words() # <class 'dict'>
    post_with_links = []
    for post in post_content:
        for word in tagged_words:
            if word in post["content"]:
                new_post = word.replace(word,f"<a href='/tag/{word}'>#{word}</a>")
                post_with_links.append(new_post)
    return post_with_links


def load_bookmarks_from_json(): #ok
    """
    Загружает все закладки из файла json
    """
    with open(os.path.join("data", "bookmarks.json"), "r", encoding="utf-8") as file:
        bookmarks = json.load(file)
        return bookmarks

def add_bookmark(post_id):
    """
    Записывает новую закладку в файл
    """
    bookmarks = load_bookmarks_from_json()
    post = get_post_by_pk(post_id)
    if post not in bookmarks:
        bookmarks.append(post)
    with open (os.path.join("data", "bookmarks.json"), "w", encoding="utf-8") as file:
        json.dump(bookmarks, file, ensure_ascii=False)
    return post


def delete_bookmark_by_post_id(post_id):
    
    """Удаляет закладку с указанным pk из файла"""

    bookmarks = load_bookmarks_from_json()
    for bookmark in bookmarks:
        if bookmark["pk"] == post_id:
            bookmarks.remove(bookmark)
    with open (os.path.join("data", "bookmarks.json"), "w", encoding="utf-8") as file:
        json.dump(bookmarks, file, ensure_ascii=False)
    return bookmarks





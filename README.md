### Moviedb-API
REST API для MVP сервиса по поиску фильмов. 
***
### Использованные технологии
* Flask 2.2.2
* Jinja2 3.1.2
* pytest 7.2.0


Доступный функционал:
* Лента со всеми постами пользователей. Для каждого выводится его автор, превью текста поста(50 символов),
количество просмотров, ссылка на поста, в шапке ссылка-флажок для перехода в закладки.
* Страничка с подробной информацией про пост. Фото, текст поста и карточка автора берутся из данных поста(данные загружаются из JSON-файла. Комментарии загружаются из файла с комментариями. Ссылка "назад" ведет на главную страницу
* Форма поиска.
* Отображение всех постов пользователя.
* Вывод всех постов по тегам.

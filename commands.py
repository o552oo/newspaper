# py manage.py shell --> Запуск shell

# from newapp.models import *  # --> импортируем модели
# User1 = User.objects.create(username='Denis', first_name ='Sidis') --> Создаём юзера
# Author.objects.create(authorUser=User1) --> Делаем юзера автором
# User2 = User.objects.create(username='Maxim', first_name ='Sidis') --> Создаём 2 юзера
# Author.objects.create(authorUser=User2) --> Делаем юзера автором
# Category.objects.create(name='Python') --> Создаём категорию
# Category.objects.create(name='Django') --> Создаём категорию
# Category.objects.create(name='JS') --> Создаём категорию
# Category.objects.create(name='OOP') --> Создаём категорию
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Denis')), categoryType='NW', title='новость_1', text='тестовая новость 1') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Maxim')), categoryType='AR', title='новость 2', text='тестовая новость 2') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Maxim')), categoryType='AR', title='новость 3', text='тестовая новость 3') --> Создаём пост
# post1 = Post.objects.get(pk=1) --> Получаем пост через primary key
# post2 = Post.objects.get(pk=2)
# post3 = Post.objects.get(pk=3)
# cat1 = Category.objects.get(name='Python') --> Получаем категорию через name
# cat2 = Category.objects.get(name='Django')
# post1.postCategory.add(cat1) --> Добавляем связи
# post1.postCategory.add(cat1, cat2) --> Добавляем связи. Т.к. many to many можно связывать несколько
# post1.postCategory.add(cat2)
# Comment.objects.create(commentUser=User.objects.get(username='Denis'), commentPost=Post.objects.get(pk=1), text='коммент1 ') --> Создаем комментарий
# Comment.objects.create(commentUser=User.objects.get(username='Denis'), commentPost=Post.objects.get(pk=2), text='коммент 2')
# Comment.objects.create(commentUser=User.objects.get(username='Maxim'), commentPost=Post.objects.get(pk=3), text='коммент 3')
# Post.objects.get(pk=1).like() --> Ставим лайки постам
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=3).dislike() --> Ставим дизлайки
# Comment.objects.get(pk=1).like() --> Ставим лайки комментам
# Comment.objects.get(pk=2).dislike() --> Ставим дизлайки комментам
# Author.objects.get(authorUser=User.objects.get(username='Denis')). update_rating() --> Обновляем рейтинг Denis
# Author.objects.get(authorUser=User.objects.get(username='Maxim')). update_rating() --> Обновляем рейтинг Maxim
# a = Author.objects.get(authorUser=User.objects.get(username='Denis'))
# a.ratingAuthor --> смотрим обновленный рейтинг
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0] --> username автора, рейтинг. Индекс первого объекта. [0:5] Весь рейтинг до 5 индекса
# print(best)
# d = User.objects.all().values('username', 'date_joined') --> даты добавления, username
# print(d)
# best_post = Post.objects.all().order_by('-rating').values('id','dateCreation', 'rating', 'author_id')[0] --> получили id дгчшего поста
# prev = Post.objects.get(id=best_post['id']).preview() --> Превью
# post_user = User.objects.get(id=best_post['author_id']) --> автор
# print(f"Лучшая статья\n Автор: {post_user},\n Дата добавления: {best_post['dateCreation']},\n Рейтинг статьи: {best_post['rating']},\n {prev}")
# comment_post = Comment.objects.get(id=best_post['id']).post_com() --> Коментарий к лучшей статье
# print(comment_post)
#
#

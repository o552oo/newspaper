from django.views.generic import ListView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post


class NewsList(List.View):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'



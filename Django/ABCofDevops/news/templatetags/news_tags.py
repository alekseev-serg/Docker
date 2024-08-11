"""
Создаём пользовательские теги
"""
from django import template

from news.models import Category

register = template.Library()  # Регистрация тега get_categories


@register.simple_tag()
def get_categories():
    return Category.objects.all()


"""
Тэг, который сам отрисовывает шаблон, эти теги равноценные, можно использовать на выбор.
"""
# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     return {"categories": categories}

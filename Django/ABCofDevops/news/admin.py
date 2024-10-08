from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    """
    Кастомизация админки в модели News
    """
    list_display = ('id', 'title', 'category', 'photo', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """
    Кастомизация админки в модели Category
    """
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from app.book.models import Book
from django.utils.html import mark_safe
# Register your models here.

def image_preview(obj, field_name='image'):
    if getattr(obj, field_name):
        return mark_safe(f'<img src="{getattr(obj, field_name).url}"width="100"/>')
    return 'Нет Изображений'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'image_preview']
    search_fields = ['id', 'title', 'author']
    list_filter = ['id', 'title', 'author']

    def image_preview(self, obj):
        return image_preview(obj, 'image')
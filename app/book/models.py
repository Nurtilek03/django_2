from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=155,
                             verbose_name='Заголовок')
    author = models.CharField(max_length=155,verbose_name='Автор')
    description = RichTextField(verbose_name='Описание')
    publish_date = models.DateField(verbose_name='Дата создание')
    image = models.ImageField(upload_to='book', verbose_name='фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Книги'
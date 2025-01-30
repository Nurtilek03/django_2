from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155)
    description = RichTextField()
    title_cool = models.CharField(max_length=155)
    description_cool = RichTextField(verbose_name='Описание cool')
    title_mussion = models.CharField(max_length=155)
    image_mussion = models.ImageField(upload_to='settings')
    title_team = models.CharField(max_length=155)
    title_avenser = models.CharField(max_length=155)
    title_works = models.CharField(max_length=155)
    title_testimonials = models.CharField(max_length=155)
    title_about = models.CharField(max_length=155)
    title_contact = models.CharField(max_length=155)
    title_have = models.CharField(max_length=155)
    description_contact = RichTextField(verbose_name='Описание контакта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройка Главной Страницы'

class Do(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'
    )
    value = models.CharField(
        max_length=155,
        verbose_name='значение'
    )
    value2 = models.CharField(
        max_length=155,
        verbose_name='значение'
    )
    value3 = models.CharField(
        max_length=155,
        verbose_name='значение'
    )
    value4 = models.CharField(
        max_length=155,
        verbose_name='значение'
    )
    value5 = models.CharField(
        max_length=155,
        verbose_name='значение'
    )
    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Что мы делаем'
    
class Ceo(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Генеральный директор'

class Founder(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Основатель'

class Designer(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Дизайнер'

class Developer(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Разработчик'


class Games(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Игры'


class Games2(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Игры-2'


class Games3(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Игры-3'

class Games4(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Игры-4'


class Games5(models.Model):
    title =models.CharField(
        max_length=155,
        verbose_name='заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Игры-5'

class Contact(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    title2 =models.CharField(
        max_length=155,
        verbose_name='Заголовок 2'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'свяжитесь с нами'

class Will_talk(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'давай поговорим с нами'

class Phone(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Телефон номер'
        
class Email(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Email'

class Address(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Адресс'
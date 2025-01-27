from django.db import models

class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    image = models.ImageField(
        upload_to="settings/",
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to="settings/",
        verbose_name='Фото 2'
    )
    job = models.CharField(
        max_length=155,
        verbose_name='Где работает'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Info(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Информация'

class About(models.Model):
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
        verbose_name_plural = 'О нас'


class Data(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    age = models.CharField(
        max_length=155,
        verbose_name='Возрасть'
    )
    occupation = models.CharField(
        max_length=155,
        verbose_name='Занятие'
    )
    phone = models.CharField(
        max_length=155,
        verbose_name='Номер Телефона'
    )

    email = models.CharField(
        max_length=155,
        verbose_name='Email'
    )
    nationality = models.CharField(
        max_length=155,
        verbose_name='Националность'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Данные'

class Creator(models.Model):
    key = models.CharField(
       max_length=155,
       verbose_name='ключ' 
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Создатель'

class End_Work(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Последний_работы'

class Design(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Веб дизайн'

class Development(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Разработка'

class Branding(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Брендинг'

class Photography(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.CharField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Фотография'

class Fun_facts (models.Model):
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
        verbose_name_plural = 'Интересные факты'

class Custom_CMS(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value2 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value3 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Пользовательская CMS'

class Custom_CMS2(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value2 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value3 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Пользовательская CMS'

class Custom_CMS3(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value2 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value3 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Пользовательская CMS'

class Custom_CMS4(models.Model):
    key = models.CharField(
        max_length=155,
        verbose_name='ключ'   
    )
    value = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value2 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    value3 = models.TextField(
        max_length=155,
        verbose_name='Значение'
    )
    image = models.ImageField(
        upload_to='info',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.key
    class Meta:
        verbose_name_plural = 'Пользовательская CMS'
# Generated by Django 5.1.5 on 2025-01-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_development'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=155, verbose_name='ключ')),
                ('value', models.CharField(max_length=155, verbose_name='Значение')),
                ('image', models.ImageField(upload_to='info', verbose_name='Фото')),
            ],
            options={
                'verbose_name_plural': 'Брендинг',
            },
        ),
    ]

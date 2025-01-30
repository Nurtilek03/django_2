# Generated by Django 4.2 on 2025-01-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_designer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='заголовок')),
                ('title2', models.CharField(max_length=155, verbose_name='заголовок 2')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Разработчик',
            },
        ),
    ]

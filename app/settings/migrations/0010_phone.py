# Generated by Django 4.2 on 2025-01-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_will_talk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Телефон номер',
            },
        ),
    ]

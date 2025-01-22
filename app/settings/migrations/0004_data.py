# Generated by Django 5.1.5 on 2025-01-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя')),
                ('age', models.CharField(max_length=155, verbose_name='Возрасть')),
                ('occupation', models.CharField(max_length=155, verbose_name='Занятие')),
                ('phone', models.CharField(max_length=155, verbose_name='Номер Телефона')),
                ('email', models.CharField(max_length=155, verbose_name='Email')),
                ('nationality', models.CharField(max_length=155, verbose_name='Националность')),
            ],
            options={
                'verbose_name_plural': 'Данные',
            },
        ),
    ]

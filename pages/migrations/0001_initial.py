# Generated by Django 3.1.1 on 2020-10-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страница О компании',
                'verbose_name_plural': 'Страница О компании',
            },
        ),
    ]
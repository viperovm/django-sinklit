# Generated by Django 3.1.1 on 2020-10-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201003_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle_ru',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
    ]

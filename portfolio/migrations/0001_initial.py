# Generated by Django 3.1.1 on 2020-10-03 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='description')),
                ('og_title', models.CharField(blank=True, max_length=250, verbose_name='og:title')),
                ('og_description', models.CharField(blank=True, max_length=250, verbose_name='og:description')),
                ('og_url', models.CharField(blank=True, max_length=250, verbose_name='og:url')),
                ('og_image', models.CharField(blank=True, max_length=250, verbose_name='og:image')),
                ('og_type', models.CharField(blank=True, default='website', max_length=250, verbose_name='og:type')),
                ('meta1', models.CharField(blank=True, max_length=250, verbose_name='Свой html перед /head')),
                ('meta2', models.CharField(blank=True, max_length=250, verbose_name='Свой html после body')),
                ('meta3', models.CharField(blank=True, max_length=250, verbose_name='Свой html перед /body')),
            ],
            options={
                'verbose_name': 'Сео настройка страницы',
                'verbose_name_plural': 'Сео настройка страницы',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=150, verbose_name='Подзаголовок')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
            options={
                'verbose_name': 'Изображение Портфолио',
                'verbose_name_plural': 'Изображения Портфолио',
            },
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_about_img_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение страницы'),
        ),
    ]

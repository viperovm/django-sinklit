# Generated by Django 3.1.1 on 2020-10-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20201005_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='numbers',
            name='background_img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображения подложки'),
        ),
        migrations.AddField(
            model_name='numbers',
            name='background_img_alt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Alt тег изображения подложки'),
        ),
        migrations.AddField(
            model_name='quote',
            name='background_img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображения подложки'),
        ),
        migrations.AddField(
            model_name='quote',
            name='background_img_alt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Alt тег изображения подложки'),
        ),
        migrations.AlterField(
            model_name='intro',
            name='img',
            field=models.ManyToManyField(blank=True, to='home.SectionImages', verbose_name='Изображения раздела'),
        ),
        migrations.AlterField(
            model_name='numbers',
            name='img',
            field=models.ManyToManyField(blank=True, to='home.SectionImages', verbose_name='Изображения раздела'),
        ),
        migrations.AlterField(
            model_name='pros',
            name='img',
            field=models.ManyToManyField(blank=True, to='home.SectionImages', verbose_name='Изображения раздела'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='img',
            field=models.ManyToManyField(blank=True, to='home.SectionImages', verbose_name='Изображения раздела'),
        ),
        migrations.AlterField(
            model_name='requestsection',
            name='img',
            field=models.ManyToManyField(blank=True, to='home.SectionImages', verbose_name='Изображения раздела'),
        ),
        migrations.AlterField(
            model_name='sectionimages',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображения раздела'),
        ),
    ]

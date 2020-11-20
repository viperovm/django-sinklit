# Generated by Django 3.1.1 on 2020-10-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_pageseo'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='meta1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Свой html перед /head'),
        ),
        migrations.AddField(
            model_name='news',
            name='og_description',
            field=models.CharField(blank=True, max_length=250, verbose_name='og:description'),
        ),
        migrations.AddField(
            model_name='news',
            name='og_image',
            field=models.CharField(blank=True, max_length=250, verbose_name='og:image'),
        ),
        migrations.AddField(
            model_name='news',
            name='og_title',
            field=models.CharField(blank=True, max_length=250, verbose_name='og:title'),
        ),
        migrations.AddField(
            model_name='news',
            name='og_type',
            field=models.CharField(blank=True, default='website', max_length=250, verbose_name='og:type'),
        ),
        migrations.AddField(
            model_name='news',
            name='og_url',
            field=models.CharField(blank=True, max_length=250, verbose_name='og:url'),
        ),
        migrations.AddField(
            model_name='news',
            name='page_description',
            field=models.CharField(blank=True, max_length=250, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='news',
            name='page_title',
            field=models.CharField(blank=True, max_length=250, verbose_name='title'),
        ),
    ]
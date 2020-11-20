from django.db import models
from django.urls import reverse


class PageSeo(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name='title')
    description = models.CharField(max_length=250, blank=True, verbose_name='description')
    og_title = models.CharField(max_length=250, blank=True, verbose_name='og:title')
    og_description = models.CharField(max_length=250, blank=True, verbose_name='og:description')
    og_url = models.CharField(max_length=250, blank=True, verbose_name='og:url')
    og_image = models.CharField(max_length=250, blank=True, verbose_name='og:image')
    og_type = models.CharField(max_length=250, blank=True, default='website', verbose_name='og:type')
    meta1 = models.CharField(max_length=250, verbose_name='Свой html перед /head', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сео настройка страницы'
        verbose_name_plural = 'Сео настройка страницы'


class PortfolioPage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=150, verbose_name='Подзаголовок', blank=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    content = models.TextField(blank=True, verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница портфолио'
        verbose_name_plural = 'Страница портфолио'


class Portfolio(models.Model):
    page_title = models.CharField(max_length=250, blank=True, verbose_name='title')
    page_description = models.CharField(max_length=250, blank=True, verbose_name='description')
    og_title = models.CharField(max_length=250, blank=True, verbose_name='og:title')
    og_description = models.CharField(max_length=250, blank=True, verbose_name='og:description')
    og_url = models.CharField(max_length=250, blank=True, verbose_name='og:url')
    og_image = models.CharField(max_length=250, blank=True, verbose_name='og:image')
    og_type = models.CharField(max_length=250, blank=True, default='website', verbose_name='og:type')
    meta1 = models.CharField(max_length=250, verbose_name='Свой html перед /head', blank=True)
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=150, verbose_name='Подзаголовок', blank=True)
    slug = models.SlugField(max_length=70, verbose_name='URL', unique=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['-created_at']


class PortfolioImage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение Портфолио'
        verbose_name_plural = 'Изображения Портфолио'
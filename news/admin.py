from django import forms
from django.contrib import admin
from .models import News, PageSeo
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class NewsAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание(ру)', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Содержание(анг)', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PageSeo)

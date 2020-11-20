from django import forms
from django.contrib import admin
from .models import About, PageSeo
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class AboutAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание(ру)', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Содержание(анг)', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    form = AboutAdminForm


admin.site.register(PageSeo)

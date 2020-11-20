from django import forms
from django.contrib import admin
from .models import Services
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class ServicesAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание(ру)', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Содержание(анг)', widget=CKEditorUploadingWidget())

    class Meta:
        model = Services
        fields = '__all__'


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    form = ServicesAdminForm
    prepopulated_fields = {'slug': ('title',)}

from django import forms
from django.contrib import admin
from .models import Portfolio, PageSeo, PortfolioPage, PortfolioImage
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class PortfolioAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание(ру)', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Содержание(анг)', widget=CKEditorUploadingWidget())

    class Meta:
        model = Portfolio
        fields = '__all__'


@admin.register(Portfolio)
class PortfolioAdmin(TranslationAdmin):
    form = PortfolioAdminForm
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PageSeo)
admin.site.register(PortfolioPage)
admin.site.register(PortfolioImage)

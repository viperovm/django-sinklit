from django import forms
from django.contrib import admin
from .models import PageSeo, Request, Intro, ServicesSection, Pros, ProsElements, Quote, Numbers, NumbersElements, RequestSection, SectionImages, ReviewsSection
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class IntroAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Содержание(ру)', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Содержание(анг)', widget=CKEditorUploadingWidget())

    class Meta:
        model = Intro
        fields = '__all__'


@admin.register(Intro)
class IntroAdmin(TranslationAdmin):
    form = IntroAdminForm


@admin.register(ServicesSection)
class ServicesSectionAdmin(TranslationAdmin):
    pass


@admin.register(Pros)
class ProsAdmin(TranslationAdmin):
    pass


@admin.register(ProsElements)
class ProsElementsAdmin(TranslationAdmin):
    pass


@admin.register(Quote)
class QuoteAdmin(TranslationAdmin):
    pass


@admin.register(Numbers)
class NumbersAdmin(TranslationAdmin):
    pass


@admin.register(NumbersElements)
class NumbersElementsAdmin(TranslationAdmin):
    pass


@admin.register(RequestSection)
class RequestSectionAdmin(TranslationAdmin):
    pass

@admin.register(ReviewsSection)
class ReviewsSectionAdmin(TranslationAdmin):
    pass


admin.site.register(PageSeo)
admin.site.register(Request)
admin.site.register(SectionImages)

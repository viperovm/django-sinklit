from modeltranslation.translator import register, TranslationOptions
from .models import Services


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')

from modeltranslation.translator import register, TranslationOptions
from .models import Reviews


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'content')

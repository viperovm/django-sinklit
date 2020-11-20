from modeltranslation.translator import register, TranslationOptions
from .models import PortfolioPage, Portfolio


@register(PortfolioPage)
class PortfolioPageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')

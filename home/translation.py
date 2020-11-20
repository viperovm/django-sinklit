from modeltranslation.translator import register, TranslationOptions
from .models import Intro, Pros, ProsElements, Quote, Numbers, NumbersElements, RequestSection, ServicesSection, ReviewsSection


@register(Intro)
class IntroTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(ServicesSection)
class ServicesSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(Pros)
class ProsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(ProsElements)
class ProsElementsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(Quote)
class QuoteTranslationOptions(TranslationOptions):
    fields = ('text', 'author')


@register(Numbers)
class NumbersTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(NumbersElements)
class NumbersElementsTranslationOptions(TranslationOptions):
    fields = ('number', 'text')


@register(RequestSection)
class RequestSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')\


@register(ReviewsSection)
class ReviewsSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')

from django.shortcuts import render
from .models import *


def about(request):
    about_page = About.objects.first()
    seo = PageSeo.objects.first()

    context = {
        'about': about_page,
        'seo': seo,
    }
    return render(request, 'about/about.html', context)

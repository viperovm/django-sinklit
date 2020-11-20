from django.shortcuts import render, redirect
from .models import *
from services.models import *
from reviews.models import *
from .forms import RequestForm
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse


# def index(request):
#     services = Services.objects.all()
#     reviews = Reviews.objects.all()
#
#     context = {
#         'title': 'Главная страница',
#         'services': services,
#         'reviews': reviews,
#     }
#     return render(request, 'home/index.html', context)


def index(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Письмо отправлено!')
            return redirect(reverse('request').replace('%23', '#'))
            # mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'yii2_loc@ukr.net', ['matroskin978@gmail.com'], fail_silently=True)
            # if mail:
            #     messages.success(request, 'Письмо отправлено!')
            #     return redirect('home')
            # else:
            #     messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
            return redirect(reverse('request').replace('%23', '#'))
    else:
        form = RequestForm()

    seo = PageSeo.objects.first()
    intro = Intro.objects.first()
    services_section = ServicesSection.objects.first()
    reviews_section = ReviewsSection.objects.first()
    pros = Pros.objects.first()
    pros_elements = ProsElements.objects.all()
    quote = Quote.objects.first()
    numbers = Numbers.objects.first()
    numbers_elements = NumbersElements.objects.all()
    request_section = RequestSection.objects.first()
    services = Services.objects.all()
    reviews = Reviews.objects.all()

    context = {
        'seo': seo,
        'intro': intro,
        'services_section': services_section,
        'reviews_section': reviews_section,
        'pros': pros,
        'pros_elements': pros_elements,
        'quote': quote,
        'numbers': numbers,
        'numbers_elements': numbers_elements,
        'request_section': request_section,
        'services': services,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'home/index.html', context)

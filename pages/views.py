from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            # form.save()
            # messages.success(request, 'Письмо отправлено!')
            # return redirect(reverse('request').replace('%23', '#'))
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
        form = ContactForm()

    context = {
        'title': 'Контакты',
        'form': form,
    }
    return render(request, 'pages/contact.html', context)

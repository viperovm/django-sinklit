from django.views.generic import ListView, DetailView

from .models import Services


class Service(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Услуги')
        return context

    def get_queryset(self):
        return Services.objects.all()


class ServiceView(DetailView):
    model = Services
    context_object_name = 'services_item'

from django.template.context_processors import request
from services.models import Services


def menu(request):
    services = Services.objects.all()

    return {"services_list": services}

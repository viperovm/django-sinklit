from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>', ServiceView.as_view(), name='view_service'),
]

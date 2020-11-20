from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsAll.as_view(), name='view_news'),
    path('<slug>', NewsOne.as_view(), name='view_news'),
]
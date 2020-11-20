from django.urls import path
from .views import *

urlpatterns = [
    path('', ReviewsAll.as_view(), name='view_reviews'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', portfolio_page, name='portfolio'),
    path('<slug>', portfolio_case, name='view_portfolio'),
]
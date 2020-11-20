from django import forms
from .models import Request
from services.models import Services
import re
from django.core.exceptions import ValidationError


class RequestForm(forms.ModelForm):
    service = forms.ModelChoiceField(empty_label='Выберите услугу*', label='Услуги',
                                      queryset=Services.objects.all(),
                                      widget=forms.Select(attrs={"class": "mdb-select md-form"}))

    class Meta:
        model = Request
        fields = ['name', 'email', 'phone', 'company_name', 'service']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

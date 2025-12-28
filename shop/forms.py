from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order
import re

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class OrderCreateForm(forms.ModelForm):
    phone = forms.CharField(max_length=18, label="Номер телефона",
                           widget=forms.TextInput(attrs={'placeholder': '+7 (7__) ___-__-__'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'address': forms.TextInput(attrs={'placeholder': 'Улица, дом, квартира'}),
            'city': forms.TextInput(attrs={'value': 'Алматы', 'readonly': 'readonly'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        digits = re.sub(r'\D', '', phone)
        if len(digits) < 11:
            raise forms.ValidationError("Введите корректный номер телефона РК")
        return phone
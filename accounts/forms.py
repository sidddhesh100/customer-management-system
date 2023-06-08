from django.forms import ModelForm
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta(object):
        model = Order
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password1", "password2"]

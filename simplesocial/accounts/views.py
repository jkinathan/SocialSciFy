from django.shortcuts import render
from accounts.models import User
from django.urls import reverse_lazy #if you are logged in or logged out where you shud actually go
from . import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
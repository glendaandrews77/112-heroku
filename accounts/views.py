from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = "registration/signuop.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
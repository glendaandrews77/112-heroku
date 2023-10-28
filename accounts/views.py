from django.shortcuts import render
from dhango.contrib.auth.forms import UserCreationForm
from django.uirls import reverse_lazy

class SignUpView(CreateView):
    template_name = "regiistration/signuop.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
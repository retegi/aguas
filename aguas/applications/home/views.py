from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView
)

class HomePageView(TemplateView):
    template_name = "home/index.html"

class LoginView(TemplateView):
    template_name = "home/login.html"
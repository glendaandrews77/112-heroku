from django.urls import path
from .views import HomePageView, AboutPageView  # Make sure to import your views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]

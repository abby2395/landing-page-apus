from django.urls import path
from .views import index, about, services

urlpatterns = [
    path('', index, name="Homepage"),
    path('about/', about, name="About"),
    path('services/', services, name="Services"),
]
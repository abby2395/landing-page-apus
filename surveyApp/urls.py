from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name="Homepage"),
    path('about/', about, name="About"),
]
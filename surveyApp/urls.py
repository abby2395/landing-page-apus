from django.urls import path
from .views import index, about, services, contact, survey

urlpatterns = [
    path('', index, name="Homepage"),
    path('about/', about, name="About"),
    path('services/', services, name="Services"),
    path('contact/', contact, name="Contact"),
    path('survey', survey, name = "Survey")
]
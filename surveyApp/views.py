from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'portfolio.html', {})

def contact(request):
    contact = Contact.objects.all()
    return render(request, 'contact.html', {contact})

def survey(request):
    return render(request, 'survey.html', {})
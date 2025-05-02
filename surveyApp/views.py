from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'portfolio.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})

def contact(request):
    if request.method == 'POST':
        form = forms.ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': forms.ContactUs(), 'success': True})
    else:
        form = forms.ContactUs()
    return render(request, 'contact.html', {'form': form})

def survey(request):
    return render(request, 'survey.html', {})
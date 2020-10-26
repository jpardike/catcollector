from django.shortcuts import render
from django.http import HttpResponse
from .models import cats

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', { 'cats': cats })
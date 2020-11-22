from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

def index(request):
    courses = Course.objects.all();
    return render(request, 'courses/index.html', {"courses": courses})

def new(request):
    return render(request, 'courses/new.html')
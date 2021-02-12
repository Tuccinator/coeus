from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Project
from .forms import NewProjectForm

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        form = NewProjectForm()
    else:
        form = NewProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.create_project(form.cleaned_data['name'], form.cleaned_data['slug'], form.cleaned_data['description'])

            return HttpResponseRedirect('/projects/' + project.slug)

    return render(request, 'projects/new.html', { 'form': form })
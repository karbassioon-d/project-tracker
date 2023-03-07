from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects
    }
    return render(request, "projects/list_projects.html", context)


def home(request):
    return redirect("list_projects")

@login_required
def show_project(request, id):
    show_project = Project.objects.get(id=id)

    context = {
        'show_project': show_project
    }

    return render(request, 'projects/details.html', context)

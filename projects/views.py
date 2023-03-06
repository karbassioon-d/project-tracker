from django.shortcuts import render, redirect
from projects.models import Project
# Create your views here.
def list_projects(request):
    list_projects = Project.objects.all()
    context = {
        "list_projects": list_projects
    }
    return render(request, "projects/list_projects.html", context)


def home(request):
    return redirect("list_projects")

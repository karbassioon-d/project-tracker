from django.shortcuts import render, redirect
from projects.models import Project
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

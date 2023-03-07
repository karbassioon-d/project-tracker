from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

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

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)

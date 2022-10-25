from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "show_project": projects,
    }
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        "show_project": project,
    }
    return render(request, "projects/detail.html", context)

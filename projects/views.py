from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
# Create your views here.

def list_projects(request):
    projects = Project.objects.all()
    context = {
        "show_project": projects,
    }
    return render(request, "projects/list_projects.html", context)

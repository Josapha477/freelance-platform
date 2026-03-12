from django.shortcuts import render, redirect
from accounts.models.skills import Skills
from jobs.models.skillsClient import Project
from jobs.forms.gestion_project_forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def project_view(request):
    projects = Project.objects.filter(status="open")
    return render(request, "pages/page_list_project.html", {"projects": projects})




@login_required
def create_project_view(request):
    skills = Skills.objects.all()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            form.save_m2m()
            return redirect("/dashboard_client")
    else:
        form = ProjectForm()
    return render(request, "creation/page_add_project.html", {"form": form, "skills": skills})


@login_required
def update_project_view(request, project_pk):
    return render(request, "")


@login_required
def delete_project_view(request, project_pk):
    return render(request, "")

@login_required
def get_project_client(request):
    projects = request.user.project_client.all()
    return render(request, "pages/list_project_client.html", {"projects": projects})
from django.shortcuts import render, redirect
from accounts.models.skills import Skills
from accounts.models.profileFreelance import ProfileFreelance
from django.contrib.auth.decorators import login_required



@login_required
def add_skills_view(request):
    if request.method == 'POST':
        skills_ids = request.POST.getlist('skills_pk')
        profile = ProfileFreelance.objects.get(user=request.user)
        profile.skills.set(skills_ids)
        profile.save()
        return redirect("/dashboard")


    skills = Skills.objects.all()
    return render(request, "creation/add_skills.html", {"skills": skills})

@login_required
def update_skills_view(request):
    if request.method == 'POST':
        skills_ids = request.POST.getlist('skills_pk')
        print(skills_ids)
        profile = ProfileFreelance.objects.get(user=request.user)
        profile.skills.set(skills_ids)
        profile.save()
        return redirect("/dashboard")
    return redirect("/dashboard")
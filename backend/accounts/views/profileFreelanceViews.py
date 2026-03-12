from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from accounts.forms.formProfile import ProfileFreelanceForm
from django.contrib.auth.decorators import login_required
from accounts.models.skills import Skills
from accounts.models.profileFreelance import (
    ProfileFreelance, 
    Certificate,
    ExperienceProfesional,
    TrainingAndStudy
)



@login_required
def createprofilefreelanceview(request):
    if request.user.user_types != "freelance":
        return redirect("/")
    try:
        profile = ProfileFreelance.objects.get(user=request.user)
        return redirect("/")
    except ProfileFreelance.DoesNotExist:
        pass
        
    if request.method == "POST":
        form = ProfileFreelanceForm(request.POST, request.FILES)
        if form.is_valid():
            profilefrelance = form.save(commit=False)
            profilefrelance.user = request.user
            profilefrelance.save()
            return redirect("/dashboard")
    else:
        form = ProfileFreelanceForm()
    return render(request, "profile/createprofilefreelance.html", {"skills": Skills.objects.all()})




def updateprofilefreelanceview(request, profilefreelance_pk):
    pass






from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models.profileFreelance import ProfileFreelance
from accounts.models.profileClient import ProfileClient
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from jobs.models.skillsClient import Project
from jobs.models.proposals import Proposal


@require_GET
@login_required
def dashboard_freelance(request):
    user_type = request.user.user_types
    if user_type.lower() != "freelance":
        return redirect('/')
    try:
        profile = ProfileFreelance.objects.get(user=request.user)
        proposals = Proposal.objects.filter(freelancer=request.user)
    except ProfileFreelance.DoesNotExist:
        return redirect('/createprofilefreelance')
    
    return render(request, "pages/dashboard-freelance.html", {"profile": profile, "proposals": proposals})



@require_GET
@login_required
def dashboard_client(request):
    user_type = request.user.user_types
    if user_type.lower() != "client":
       return redirect("/")
    try:
        profile = ProfileClient.objects.get(user=request.user)
        project_all = request.user.project_client.all()
        contract_all = request.user.contract_client.all()
    except ProfileClient.DoesNotExist:
        return redirect("/createprofileclient")

    return render(request, "pages/dashboard_client.html", {'profile': profile, "project": project_all, "contract": contract_all})


 
def list_freelance_view(request):

    return render(request, 'pages/page_freelance.html', {})


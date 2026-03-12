from django.shortcuts import render, redirect
from jobs.forms.gestion_proposals_form import ProposalForm
from jobs.models.skillsClient import Project
from django.contrib.auth.decorators import login_required
from jobs.models.proposals import Proposal

@login_required
def create_proposal_view(request, project_pk):
    project = Project.objects.get(pk=project_pk)

    if request.method == "POST":
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.project = project
            proposal.freelancer = request.user
            proposal.save()
            return redirect("/dashboard_freelance")
    else:
        form = ProposalForm()

    return render(request, "creation/page_add_proposal.html", {"project": project, "form": form})



@login_required
def get_proposal_project(request, project_pk):
    project = Project.objects.get(client=request.user, pk=project_pk)
    proposals = project.proposal_project.all()  # type: ignore
    return render(request, "pages/page_proposals.html", {"proposals": proposals})

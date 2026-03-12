from django.shortcuts import render, redirect
from jobs.models.contrats import Contract
from jobs.models.skillsClient import Project
from jobs.models.proposals import Proposal
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from accounts.models.users import CustomUser


@require_POST
@login_required
def create_contract(request, proposal_pk):
    proposals = Proposal.objects.get(pk=proposal_pk)
    freelancer = CustomUser.objects.get(pk=proposals.freelancer.pk)
    project = Project.objects.get(pk=proposals.project.pk)
    
    if proposals.is_accepted != False and project.status != "open":
        return redirect("/")

    contract = Contract.objects.create(
            project=project,
            client=request.user,
            proposal=proposals,
            freelance=freelancer,
            agreed_amount=proposals.proposed_budget,
            end_date=proposals.delivry_time,
        )
        
    contract.save()
    proposals.is_accepted = True
    project.status = "in_progress"
    proposals.save()
    project.save()
    return redirect(f"/contract_detail/{contract.pk}")





@require_GET
@login_required
def contract_client_detail(request, contract_pk):
    contract = Contract.objects.get(client=request.user, pk=contract_pk)
    return render(request, "detail/contract-detail.html", {"contract": contract})



@require_GET
@login_required
def contract_client_view(request):
    if request.user.user_types != 'client':
        return redirect("/")
    contracts = Contract.objects.filter(client=request.user)
    return render(request, "pages/page_contract.html", {"contracts": contracts, })



def send_mail(user, email, title, message):
    return ""



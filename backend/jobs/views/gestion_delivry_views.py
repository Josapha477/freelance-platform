from django.shortcuts import render, redirect
from jobs.forms.gestion_delivry_forms import DelivryForm
from jobs.models.contrats import Contract
from django.contrib.auth.decorators import login_required


@login_required
def create_delivry_view(request, contract_pk):
    contract = Contract.objects.get(contract_pk)
    if request.method == "POST":
        form = DelivryForm(request.POST, request.FILES)
        if form.is_valid():
            delivry = form.save(commit=False)
            delivry.contract = contract
            delivry.freelance = request.user
            return redirect("dashboard")
    else: 
        form = DelivryForm()
    return render(request, "creation/page_add_delivry.html", {"contract": contract, "form": form})


@login_required
def update_delivry_view(request, delivry_pk):
    return render(request, "")



@login_required
def delete_delivry_view(request, delivry_pk):
    return render(request, "")




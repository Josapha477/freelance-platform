from django import forms
from jobs.models.proposals import Proposal



class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = (
            "proposed_budget",
            "delivry_time",
            "cover_letter",
        )



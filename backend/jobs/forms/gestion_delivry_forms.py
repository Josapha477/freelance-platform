from django import forms
from jobs.models.deliverys import Delivery



class DelivryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['message', 'files']
        
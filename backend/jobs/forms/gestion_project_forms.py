from typing import Any
from django import forms
from jobs.models.skillsClient import Project
from accounts.models.skills import Skills
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core import validators



class ProjectForm(forms.ModelForm):
    skills_required = forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Project
        fields = [
            "title", 
            "description",  
            "budget",
            "deadline",
            "skills_required",
            ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg "
                "focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors",
                "placeholder": "ex: Développement site e-commerce React",
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 "
                "focus:ring-blue-500 focus:border-blue-500 transition-colors",
                "placeholder": "Décrivez votre projet en détail...",
            }),
            "budget": forms.NumberInput(attrs={
                "class": "w-full pl-8 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 "
                "focus:ring-blue-500 focus:border-blue-500 transition-colors",
                "placeholder": "",
            }),
            "deadline": forms.DateInput(attrs={
                "class": "w-full pl-8 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 "
                "focus:ring-blue-500 focus:border-blue-500 transition-colors",
                "placeholder": "",
            })
        }

        label = {
            "title": "Titre du projet",
            "description": "Description détaillée",
            "budget":  "",
            "deadline": "",
        }

        error_message = {
            "title": {
                "": "",
            },
            "description": {
                "": "",
            },
            "budget": {
                "": "",
            },


        }

        
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        budget = cleaned_data.get("budget")
        deadline = cleaned_data.get("deadline")
        skills_required = cleaned_data.get("skills_required")

        if title:
            if len(title) > 20:
                raise forms.ValidationError({
                "": ""
            })
        if description:
            if len(description) >= 2000:
                pass

        return cleaned_data
    


"""
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project_client")
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="HTG")
    deadline = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='open')
    skills_required = models.ManyToManyField(Skills, related_name="project_skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
"""


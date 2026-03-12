from django.db import models
from django.conf import settings
from django.conf import settings
from accounts.models.skills import Skills
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Project(models.Model):
    STATUS_CHOICES = [
        ('open', "Open for Proposals"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project_client")
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    budget = models.DecimalField(max_digits=10, decimal_places=2, help_text="")
    currency = models.CharField(max_length=10, default="HTG")
    deadline = models.DateTimeField(help_text="")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='open')
    skills_required = models.ManyToManyField(Skills, related_name="project_skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project client"

    



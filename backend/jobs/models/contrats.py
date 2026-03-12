from django.db import models
from django.conf import settings
from .skillsClient import Project
from .proposals import Proposal

class Contract(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="contract_project")
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE, related_name="contract_proposal")
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contract_client")
    freelance = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contract_freelance")
    agreed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('completed', "Completed"),
        ("disputed", "Disputed"),
        
    ], default="active")

    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.conf import settings
from jobs.models.skillsClient import Project

class Proposal(models.Model):
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="proposal_freelance")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="proposal_project")
    proposed_budget = models.DecimalField(max_digits=10, decimal_places=2)
    delivry_time = models.PositiveIntegerField()
    cover_letter = models.TextField(default="")
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ("project", "freelancer")

    def __str__(self):
        return f"freelance : {self.freelancer}, projet : {self.project}"

from django.db import models
from jobs.models.contrats import Contract
from django.conf import settings


class Delivery(models.Model):
    contrat = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="contract_delivery")
    freelance = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="freelance_delivery")
    message = models.TextField(default="")
    attachments = models.FileField(upload_to="deliveries/")
    submitted_at = models.DateTimeField(auto_now_add=True)


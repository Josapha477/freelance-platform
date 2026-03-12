from django.db import models
from jobs.models.contrats import Contract
from django.conf import settings



class Review(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    reviewed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews_given")
    reviewed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews_received")
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)




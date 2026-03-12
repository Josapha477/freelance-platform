from django.db import models
from django.conf import settings

class ProfileClient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_client")
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    user_type = models.CharField(max_length=20, default="client")
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    country = models.CharField(max_length=20, default="HAITI")
    company = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client Profile"


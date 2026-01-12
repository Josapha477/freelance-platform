from django.db import models
from profiles.models import FreelanceProfile



class IdentityVerification(models.Model):
    freelance = models.OneToOneField(
        FreelanceProfile, on_delete=models.CASCADE
    )
    document = models.FileField(upload_to='identity_doc/')
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)


class SkillVerification(models.Model):
    freelance = models.ForeignKey(
        FreelanceProfile, 
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey('skills.Skills', on_delete=models.CASCADE)
from django.db import models
from django.conf import settings

class FreelanceProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to='media/avatar', blank=True)
    bio = models.TextField()
    skills = models.ManyToManyField('skills.Skills')
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.email} - {self.bio} - {self.skills} - {self.is_visible} - {self.created_at}"


class Portfolio(models.Model):
    freelance = models.ForeignKey(
        FreelanceProfile,
        on_delete=models.CASCADE,
        related_name='portfolios',
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    file = models.FileField(upload_to='portfolio', blank=True)

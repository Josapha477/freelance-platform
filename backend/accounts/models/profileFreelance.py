from django.db import models
from django.conf import settings
from .skills import Skills

class ProfileFreelance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_freelance")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20, default="freelance")
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    phone = models.CharField(max_length=15)
    balance = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=30, default="HAITI")
    bio = models.TextField(default="", null=True, blank=True)
    skills = models.ManyToManyField(Skills, related_name='competence', blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    year_experience = models.IntegerField(default=0, blank=True)
    portfolio_url = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to="cv/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Freelance Profile"



class Certificate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="certificate")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "freelance Certificate"



class ExperienceProfesional(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="freelance_experience")
    post = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=6000, default="", null=True, blank=True)
    start_month = models.DateField(null=True, blank=True)
    start_year = models.DateField(null=True, blank=True)
    end_month = models.DateField(null=True, blank=True)
    end_year = models.DateField(null=True, blank=True)
    skills = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Experience freelance"
   



class TrainingAndStudy(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="freelance_study")
    skills = models.CharField(max_length=100, null=True, blank=True)
    schools = models.CharField(max_length=100, null=True, blank=True)
    year_of_get_diploma = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=6000, default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Formation et etudes de freelance"




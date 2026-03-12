import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ("freelance", "Freelance"),
        ("client", "Client"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    user_types = models.CharField(max_length=20, choices=STATUS_CHOICES)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Utilisateur"
       

    def __str__(self):
        return self.email

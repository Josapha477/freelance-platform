from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_types = forms.ChoiceField(choices=(
        ("client", "Client"),
        ("freelance", "Freelance"),
    ))
    

    def save(self, request):
        user = super().save(request)
        user.user_types = self.cleaned_data["user_types"] # type: ignore
        user.save()
        return user



"""

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    is_freelance = models.CharField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Utilisateur"
       

    def __str__(self):
        return self.email
"""
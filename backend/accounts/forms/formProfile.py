from django.forms import ModelForm
from accounts.models.profileClient import ProfileClient
from accounts.models.profileFreelance import (
    ProfileFreelance, 
    Certificate,
    ExperienceProfesional,
    TrainingAndStudy
)

class ProfileClientForm(ModelForm):
    class Meta:
        model = ProfileClient
        fields = (
            "last_name",
            "first_name",
            "avatar",
            "phone",
            "country", 
            "company", 
            "industry",
                  )



class ProfileFreelanceForm(ModelForm):
    class Meta:
        model = ProfileFreelance
        fields = ("first_name",
                  "last_name",
                  "avatar",
                  "phone",
                  "country",
                  "bio", 
                  "skills", 
                  "hourly_rate", 
                  "year_experience",
                  "portfolio_url",
                  "cv",
                  )


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = (
            "name",
            "description",
        )


class ExperienceProfesionalForm(ModelForm):
    class Meta:
        model = ExperienceProfesional
        fields = (
            "post",
            "description",
            "start_month",
            "start_year",
            "end_year",
            "end_month",
            "skills",
        )


class  TrainingAndStudyForm(ModelForm):
    class Meta:
        model = TrainingAndStudy
        fields = (
            "skills",
            "schools",
            "year_of_get_diploma",
            "description",
        )


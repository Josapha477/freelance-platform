from rest_framework.serializers import ModelSerializer
from .models import FreelanceProfile

class FreelanceProfilSerializers(ModelSerializer):
    model = FreelanceProfile
    field = [
        'id', 'user','avatar', 'skills', 'created_at'
    ]

    def validate(self, attrs):
        return super().validate(attrs)
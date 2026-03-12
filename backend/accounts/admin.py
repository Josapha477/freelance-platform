from django.contrib import admin
from accounts.models.users import CustomUser
from accounts.models.profileFreelance import ProfileFreelance
from accounts.models.skills import Skills


admin.site.register(CustomUser)
admin.site.register(ProfileFreelance)
admin.site.register(Skills)
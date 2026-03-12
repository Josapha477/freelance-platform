from django.urls import path

from accounts.views.profileClientViews import createprofileclientview
from accounts.views.profileFreelanceViews import createprofilefreelanceview


app_name = "accounts"


urlpatterns = [
    path("createprofileclient/", createprofileclientview, name="createprofileclient"),
    path("createprofilefreelance/", createprofilefreelanceview, name="createprofilefreelance"),
]

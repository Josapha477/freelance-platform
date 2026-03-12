from django.urls import path
from jobs.views.page_profile_views import dashboard_freelance, dashboard_client
from jobs.views.page_home_views import index
from jobs.views.gestion_skills_views import add_skills_view
from jobs.views.gestion_project_views import project_view
from jobs.views.gestion_project_views import create_project_view, get_project_client
from jobs.views.gestion_proposals_views import create_proposal_view, get_proposal_project
from jobs.views.gestion_contract_view import create_contract, contract_client_view, contract_client_detail




app_name = "jobs"

urlpatterns = [
    path("", index, name="home"),
    path("dashboard_freelance/", dashboard_freelance, name="dashboardfreelance"),
    path("add_skills/", add_skills_view, name="add_skills"),
    path("dashboard_client/", dashboard_client, name="dashboardclient"),
    path("list_project/", project_view, name="list_project"),
    path("create_project/", create_project_view, name="create_project"),
    path("create_proposal/<int:project_pk>/", create_proposal_view, name = "create_proposal"),
    path("get_project_client/", get_project_client, name="get_projects_client"),
    path("get_proposal_project/<int:project_pk>/", get_proposal_project, name="get_proposal_project"),
    path("create_contract/<int:proposal_pk>", create_contract, name="create_contract"),
    path("contract_client/", contract_client_view, name="contract_client"),
    path("contract_detail/<int:contract_pk>/", contract_client_detail, name="contract_client_detail")
   
]

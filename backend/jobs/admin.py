from django.contrib import admin
from jobs.models.skillsClient import Project
from jobs.models.proposals import Proposal
from jobs.models.contrats import Contract
from jobs.models.deliverys import Delivery

admin.site.register(Project)
admin.site.register(Proposal)
admin.site.register(Contract)
admin.site.register(Delivery)



from django.contrib import admin
from .models import TeamMember, Portfolio, CustomUser, Contact, About, Service, Job, JobApplication
# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Portfolio)
admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(JobApplication)
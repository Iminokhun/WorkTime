from django.contrib import admin
from .models import Employee, Organization, WorkHours

admin.site.register(Employee)
admin.site.register(Organization)
admin.site.register(WorkHours)

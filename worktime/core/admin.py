from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
from .models import Organization, EmployeeUser, WorkHours

@admin.register(models.Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    list_display = ['name', 'stat_time', 'end_time']



@admin.register(EmployeeUser)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'login']
    list_display = ['first_name', 'last_name', 'organization', 'login']


@admin.register(WorkHours)
class WorkHoursAdmin(admin.ModelAdmin):
    list_filter = ['date', 'start_time']


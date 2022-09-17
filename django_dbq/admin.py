from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'state', 'queue_name', 'priority', 'run_after')
    list_filter =  ('name', 'state', 'queue_name', 'priority')
    search_fields = ('id', 'run_after')
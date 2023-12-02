from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'description', 'created_at')

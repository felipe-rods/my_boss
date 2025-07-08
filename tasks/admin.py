from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'description', 'deadline', 'priority')


admin.site.register(Task, TaskAdmin)

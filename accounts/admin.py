from django.contrib import admin

# Register your models here.
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'assigned_to', 'project')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'client_name', 'assigned_to', 'repo')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Note, NoteAdmin)

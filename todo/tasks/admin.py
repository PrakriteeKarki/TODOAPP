from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
    list_editable=('is_completed',)
    ordeing = ('updated_at')
    search_fields=('task',)
                    






admin.site.register(Task,TaskAdmin)
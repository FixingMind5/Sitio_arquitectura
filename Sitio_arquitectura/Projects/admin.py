from django.contrib import admin
from .models import Project, Building, UrbanSpace

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project)
admin.site.register(Building)
admin.site.register(UrbanSpace)

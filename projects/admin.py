from django.contrib import admin
from .models import Rawdata, Project, Project_Member

# Register your models here.
@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Project_Member)
class ProjectMemberAdmin(admin.ModelAdmin):
    pass
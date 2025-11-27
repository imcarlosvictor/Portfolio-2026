from django.contrib import admin

from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title']
    list_filter = ['title']
    list_editable = ['title']
    prepopulated_fields = {'slug': ('title',)}

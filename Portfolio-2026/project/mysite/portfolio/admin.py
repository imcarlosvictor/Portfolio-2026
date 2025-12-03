from django.contrib import admin

from .models import Project, ProjectMedia

# Register your models here.
# @admin.register(Project)
# class ProjectsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'slug', 'title']
#     list_editable = ['title']
#     prepopulated_fields = {'slug': ('title',)}

# admin.py
class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 5  # shows 5 empty rows
    fields = ["media_type", "file", "order"]
    ordering = ["order"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ("title",)
    list_filter = ['title']
    inlines = [ProjectMediaInline]


@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "media_type", "order")
    list_filter = ("media_type", "project")
    search_fields = ("project__title",)
    ordering = ("project", "order")

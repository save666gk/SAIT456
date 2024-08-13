

from django.contrib import admin
from .models import Category, Project, CategoryNews, News, CaseCard, CategoryTag

admin.site.register(Category)
admin.site.register(CategoryNews)
admin.site.register(News)
admin.site.register(CaseCard)
admin.site.register(CategoryTag)

from django.contrib import admin
from .models import Project, ProjectPhoto

class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]

# Отредактируйте существующую регистрацию
admin.site.register(Project, ProjectAdmin)

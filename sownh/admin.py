

from django.contrib import admin
from .models import Category, Project, CategoryNews, News, CaseCard, CategoryTag

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(CategoryNews)
admin.site.register(News)
admin.site.register(CaseCard)
admin.site.register(CategoryTag)

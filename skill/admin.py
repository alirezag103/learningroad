from django.contrib import admin

from skill import models

# Register your models here.

@admin.register(models.SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    search_fields = ['title',]

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description',]


@admin.register(models.Prerequisite)
class PrerequisiteAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skill', 'requisite']

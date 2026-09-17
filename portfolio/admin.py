from django.contrib import admin
from .models import Project, Skill, BlogPost, Resume


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "created_at")
    list_filter = ("featured",)
    search_fields = ("title", "tech_stack")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    ordering = ("category", "order")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    list_filter = ("published",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "updated_at")

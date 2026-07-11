from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    list_filter = ("author", "published_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
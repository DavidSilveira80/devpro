from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "text", "created_date", "published_date")

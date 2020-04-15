from django.contrib import admin
from post.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_published"]
    list_display_links = ["title"]
    list_editable = ["is_published"]
    search_fields = ["title", "description"]
admin.site.register(Post,PostAdmin)

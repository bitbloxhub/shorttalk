from django.contrib import admin
from shorttalk.main.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content")

admin.site.register(Post, PostAdmin)

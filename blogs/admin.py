from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'by', 'title', 'date')
    list_display_links = ('id', 'by')
admin.site.register(Post,PostAdmin)
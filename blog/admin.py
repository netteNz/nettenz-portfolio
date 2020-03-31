from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_slug', 'status','create_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'post_slug': ('title',)}
  
admin.site.register(Post, PostAdmin)
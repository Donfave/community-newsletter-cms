from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content', 'author')

    class Media:
        css = {
        'all': ('newsletter/admin.css',)
    }
    
admin.site.site_header = "Community Voice CMS"
admin.site.site_title = "Community Voice"
admin.site.index_title = "Newsletter Management"
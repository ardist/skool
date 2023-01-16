from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'writer')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('writer',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

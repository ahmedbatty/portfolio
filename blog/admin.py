from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'body', 'image', 'is_active']}),
    ]

    list_display = ('id', 'title', 'pub_date', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'body',)
    ordering = ('id',)


admin.site.register(Blog, BlogAdmin)

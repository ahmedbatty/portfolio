from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['summary', 'image', 'is_active']}),
    ]

    list_display = ('id', 'summary', 'is_active',)
    list_display_links = ('summary',)
    search_fields = ('summary',)
    ordering = ('id',)


admin.site.register(Job, JobAdmin)

from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['summary', 'image']}),
    ]

    list_display = ('id', 'summary')
    list_display_links = ('summary',)
    search_fields = ('summary',)
    ordering = ('id',)


admin.site.register(Job, JobAdmin)

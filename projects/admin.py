from django.contrib import admin

from .models import AboutPerson, PersonSocialMedia, Project


class AboutPersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['name', 'about', 'image', 'about_image_thumbnail', 'resume', 'is_active']}),
    ]
    readonly_fields = ['about_image_thumbnail']

    list_display = ('id', 'name', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('id',)


class PersonSocialMediaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['social_media', 'url', 'is_active']}),
    ]

    list_display = ('id', 'social_media', 'url')
    list_display_links = ('social_media',)
    ordering = ('id',)


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'detail', 'image', 'project_image_thumbnail', 'date', 'is_active']}),
    ]
    readonly_fields = ['project_image_thumbnail']

    list_display = ('id', 'title', 'summary', 'date_pretty', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'detail',)
    ordering = ('id',)


admin.site.register(AboutPerson, AboutPersonAdmin)
admin.site.register(PersonSocialMedia, PersonSocialMediaAdmin)
admin.site.register(Project, ProjectAdmin)

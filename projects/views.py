from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AboutPerson, PersonSocialMedia, Project


class HomeView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()
        projects = Project.objects

        context = {'about': about, 'social_medias': social_medias, 'projects': projects}

        return render(request, template_name='projects/home.html', context=context)


class ProjectView(View):
    def get(self, request, project_id, project_slug):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()
        project = get_object_or_404(Project, pk=project_id)

        context = {'about': about, 'social_medias': social_medias, 'project': project}

        return render(request, template_name='projects/project.html', context=context)


class AboutView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()

        context = {'about': about, 'social_medias': social_medias}

        return render(request, template_name='projects/about.html', context=context)


class ContactView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()

        context = {'about': about, 'social_medias': social_medias}

        return render(request, template_name='projects/contact.html', context=context)

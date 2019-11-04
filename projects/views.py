from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AboutPerson, Project


class HomeView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)
        projects = Project.objects

        context = {'about': about, 'projects': projects}

        return render(request, template_name='projects/home.html', context=context)


class ProjectView(View):
    def get(self, request, project_id):
        about = AboutPerson.objects.get(pk=1)
        project = get_object_or_404(Project, pk=project_id)

        context = {'about': about, 'project': project}

        return render(request, template_name='projects/project.html', context=context)


class AboutView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)

        context = {'about': about}

        return render(request, template_name='projects/about.html', context=context)


class ContactView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)

        context = {'about': about}

        return render(request, template_name='projects/contact.html', context=context)

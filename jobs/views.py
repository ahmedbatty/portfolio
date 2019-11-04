from django.shortcuts import render
from django.views import View

from .models import Job


class HomeView(View):
    def get(self, request):
        jobs = Job.objects

        context = {'jobs': jobs}

        return render(request, template_name='jobs/home.html', context=context)

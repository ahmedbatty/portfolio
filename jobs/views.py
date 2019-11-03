from django.shortcuts import render
from django.views import View

from .models import Job


class HomeView(View):
    def get(self, request):
        jobs = Job.objects

        return render(request, 'jobs/home.html', {'jobs': jobs})

from django.urls import path

from .views import ProjectView, AboutView, ContactView

urlpatterns = [
    # ex: /project/5/
    path('project/<int:project_id>/<slug:project_slug>', ProjectView.as_view(), name='project'),

    # ex: /about/
    path('about/', AboutView.as_view(), name='about'),

    # ex: /contact/
    path('contact/', ContactView.as_view(), name='contact'),
]

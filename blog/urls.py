from django.urls import path

from .views import BlogView, BlogPostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:blog_id>/', BlogPostView.as_view(), name='post'),
]

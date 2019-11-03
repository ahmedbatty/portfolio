from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Blog


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects

        return render(request, 'blog/blog.html', {'blogs': blogs})


class BlogPostView(View):
    def get(self, request, blog_id):
        blog_post = get_object_or_404(Blog, pk=blog_id)

        return render(request, 'blog/post.html', {'blog': blog_post})

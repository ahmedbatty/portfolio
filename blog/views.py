from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Blog


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects

        context = {'blogs': blogs}

        return render(request, template_name='blog/blog.html', context=context)


class BlogPostView(View):
    def get(self, request, blog_id):
        blog_post = get_object_or_404(Blog, pk=blog_id)

        context = {'blog_post': blog_post}

        return render(request, template_name='blog/post.html', context=context)

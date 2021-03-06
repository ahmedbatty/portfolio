from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Blog
from projects.models import AboutPerson, PersonSocialMedia


# View for all blog posts
class BlogView(View):
    def get(self, request):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()
        blogs = Blog.objects

        context = {'about': about, 'social_medias': social_medias, 'blogs': blogs}

        return render(request, template_name='blog/blog.html', context=context)


# View for one blog post
class BlogPostView(View):
    def get(self, request, blog_id, blog_slug):
        about = AboutPerson.objects.get(pk=1)
        social_medias = PersonSocialMedia.objects.all()
        blog_post = get_object_or_404(Blog, pk=blog_id)

        context = {'about': about, 'social_medias': social_medias, 'blog_post': blog_post}

        return render(request, template_name='blog/post.html', context=context)

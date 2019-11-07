from django.db import models
from django.utils.html import format_html


class AboutPerson(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    resume = models.FileField(upload_to='resume/')
    about = models.TextField(max_length=5000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def about_image_thumbnail(self):
        img = f'{self.image.url}' if self.image else 'No Thumbnail!'
        style = ''

        return format_html(f'<img style="{style}" src="{img}" alt="{img}" width="200" height="200">')


class PersonSocialMedia(models.Model):
    GITHUB = 'github'
    FACEBOOK = 'facebook-f'
    TWITTER = 'twitter'
    REDDIT = 'reddit-alien'
    LINKEDIN = 'linkedin-in'
    INSTAGRAM = 'instagram'
    YOUTUBE = 'youtube'
    SOCIAL_MEDIA_TYPES = (
        (GITHUB, 'GitHub'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (REDDIT, 'Reddit'),
        (LINKEDIN, 'LinkedIn'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'YouTube')
    )

    social_media = models.CharField(max_length=20, choices=SOCIAL_MEDIA_TYPES)
    url = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.social_media


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    detail = models.TextField(max_length=3000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.detail[:100]

    def date_pretty(self):
        return self.date.strftime('%B, %Y')

    def project_image_thumbnail(self):
        img = f'{self.image.url}' if self.image else 'No Thumbnail!'
        style = ''

        return format_html(f'<img style="{style}" src="{img}" alt="{img}" width="560" height="360">')

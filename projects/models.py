from django.db import models


class AboutPerson(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', blank=True)
    resume = models.FileField(upload_to='resume/')
    about = models.TextField(max_length=5000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')
    date = models.DateField()
    detail = models.TextField(max_length=3000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.detail[:100]

    def date_pretty(self):
        return self.date.strftime('%B, %Y')

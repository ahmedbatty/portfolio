from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

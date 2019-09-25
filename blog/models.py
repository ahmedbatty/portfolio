from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

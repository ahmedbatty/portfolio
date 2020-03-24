from django.db import models
from ckeditor.fields import RichTextField


# Model for blog post
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e, %Y')

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Model for blog post
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    body = RichTextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e, %Y')

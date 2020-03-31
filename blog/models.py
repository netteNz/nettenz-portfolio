from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create_date = models.CharField(max_length=20)
    edit_date = models.DateTimeField(auto_now=True)
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title
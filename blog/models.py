from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Pylady(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField()
    github = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    photo = models.ImageField()

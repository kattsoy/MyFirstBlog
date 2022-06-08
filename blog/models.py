from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title       = models.CharField(max_length=256)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    body        = models.TextField()

    def __str__(self):
        return f'{self.title} | {self.author}'



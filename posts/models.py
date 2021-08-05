from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    rate = models.IntegerField()
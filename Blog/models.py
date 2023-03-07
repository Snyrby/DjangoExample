from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    # blank = how the field is rendered (required or not. null = if the value can be null in the database

    def get_absolute_url(self):
        return reverse('Blog:article_detail', kwargs={'id': self.id})  # f'/product/{self.id}/'
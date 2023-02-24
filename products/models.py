from django.db import models

# Create your models here.


# in order to keep track of products
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')

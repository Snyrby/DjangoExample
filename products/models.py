from django.contrib.auth.password_validation import exceeds_maximum_length_ratio
from django.db import models
from django.urls import reverse

# Create your models here.


# in order to keep track of products
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    # blank = how the field is rendered (required or not. null = if the value can be null in the database
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField(default=False)  # in order to not get errors since other products are built with no
    # featured you can do null= true, default= true

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'id': self.id})  # f'/product/{self.id}/'


from django.db import models
from django.contrib.auth.models import User


# https://stackoverflow.com/questions/34563454/django-imagefield-upload-to-path
# the above link gives Django template rendering syntax as well

# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html



class Profile(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    preferred = models.BooleanField(default=False)

class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    inventory = models.IntegerField()
    image = models.ImageField(upload_to='static/static_dirs/media/', default='static/static_dirs/media/Hendrix.jpg')
    related_products = models.CharField(max_length=500, default=None)

class TransactionsHistory(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    transaction_total = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

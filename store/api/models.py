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
    price = models.DecimalField(decimal_places=2, max_digits=7)
    inventory = models.IntegerField()
    image = models.ImageField(upload_to='static/static_dirs/media/')

class TransactionsHistory(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    quantity_purchased = models.IntegerField()
    transaction_total = models.DecimalField(decimal_places=2, max_digits=7)
    timestamp = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()

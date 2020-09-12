from django import forms
from django.db import models
from django.contrib.auth.models import User



# https://stackoverflow.com/questions/34563454/django-imagefield-upload-to-path
# the above link gives Django template rendering syntax as well

# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html



class Profile(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    preferred = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Products(models.Model):
    CATEGORIES = [
        ('GUITARS', (
            ('ACOUSTIC', 'acoustic'),
            ('ELECTRIC', 'electric')
        )
    ),
        ('AMPS', (
            ('TUBE AMPS', 'tube'),
            ('SOLID STATE AMPS', 'solid state'),
        )
    ),
        ('CASES',(
            ('SOFT CASES', 'soft cases'),
            ('HARD CASES', 'hard cases')
        )
    ),
]

    product_name = models.CharField(max_length=30, unique=True)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    inventory = models.IntegerField()
    brand = models.CharField(max_length=50, blank=True, null=True)
    # Electric, Acoustic, Amps, Straps so users can filter by these in search
    category = models.CharField(max_length=30, choices=CATEGORIES, default="GUITARS")
    image = models.ImageField(upload_to='static/static_dirs/media/', default='static/static_dirs/media/Hendrix.jpg')
    related_products = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.product_name


class Reviews(models.Model):
    # https: // claritydev.net / blog / adding - a - blog - to - your - django - website / ----- the RichTextField
    ONE_TO_FIVE_STAR_RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products, to_field='product_name', on_delete=models.CASCADE)
    review = models.TextField(blank=True)
    product_rating = models.IntegerField(choices=ONE_TO_FIVE_STAR_RATING_CHOICES)

    def __str__(self):
        return f"{self.user}, {self.product_name}, {self.product_rating}"


class TransactionsHistory(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products, to_field='product_name', on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    transaction_total = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}, {self.product_name}, quantity: {self.quantity_purchased}, total: {self.transaction_total}, {self.timestamp}"

class Cart(models.Model):
    user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products, to_field="product_name", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user}, {self.product_name}, {self.quantity}"

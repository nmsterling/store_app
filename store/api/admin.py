from django.contrib import admin
from .models import Profile, Products, TransactionsHistory, Cart, Reviews

# Register your models here.

admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(TransactionsHistory)
admin.site.register(Cart)
admin.site.register(Reviews)

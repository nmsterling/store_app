from django.shortcuts import render
from django.contrib.auth.models import User

# https://stackoverflow.com/questions/34563454/django-imagefield-upload-to-path
# these I think we'll need for the image rendering somehow....
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from rest_framework import generics

from .serializers import ProfileSerializer, ProductsSerializer, TransactionHistorySerializer, CartSerializer
from .models import Profile, Products, TransactionsHistory, Cart

class ProfileListCreate(generics.ListCreateAPIView):

    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class ProductsListCreate(generics.ListCreateAPIView):


    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def pre_save(self, request):
        current_user = request.user
        user = User.objects.get(username=current_user)


class TransactionHistoryListCreate(generics.ListCreateAPIView):
    queryset = TransactionsHistory.objects.all()
    serializer_class = TransactionHistorySerializer

    def pre_save(self, request):
        current_user = request.user
        user = User.objects.get(username=current_user)


class CartListCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
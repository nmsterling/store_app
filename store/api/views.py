from django.shortcuts import render
from django.contrib.auth.models import User

# https://stackoverflow.com/questions/34563454/django-imagefield-upload-to-path
# these I think we'll need for the image rendering somehow....
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from rest_framework import generics

from .serializers import ProfileSerializer, ProductsSerializer, TransactionHistorySerializer, CartSerializer, ReviewsSerializer, ReviewCreateSerializer
from .models import Profile, Products, TransactionsHistory, Cart, Reviews

class ProfileListCreate(generics.ListCreateAPIView):


    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # this is how I passed a particular user to template, then Vue could grab that - we can rename it later or bag it altogether
    def pre_save(self, request):
        current_user = request.user
        user = User.objects.get(username=current_user)

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


class ReviewsList(generics.ListAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        product_name = self.kwargs['product_name']
        return Reviews.objects.filter(product_name=product_name)

class ReviewsCreate(generics.ListCreateAPIView):
    serializer_class = ReviewCreateSerializer

    def get_queryset(self):

        product_name = self.kwargs['product_name']
        return Reviews.objects.filter(product_name=product_name)


# from django documentation:
# class PurchaseList(generics.ListAPIView):
#     serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         username = self.kwargs['username']
#         return Purchase.objects.filter(purchaser__username=username)
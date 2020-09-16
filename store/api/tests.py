import json
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient, APIRequestFactory
from .models import Cart, Profile, Products, TransactionsHistory

class TestPages(TestCase):
    def test_cart(self):
        self.client = APIClient()
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        self.client = APIClient()
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)

    def test_shop(self):
        self.client = APIClient()
        response = self.client.get("/shop/")
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        self.client = APIClient()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_account(self):
        self.client = APIClient()
        response = self.client.get("/account/")
        self.assertEqual(response.status_code, 200)


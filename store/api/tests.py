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

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class ProductsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Products.objects.create(id=1,
                                product_name="Fender Telecaster",
                                product_description="American made, single-coil pickups, Deep-C profile.",
                                price="1546.99",
                                inventory=11,
                                brand="Fender",
                                category="ELECTRIC",
                                image="static/static_dirs/media/Butterscotch_tele.jpg",
                                related_products="Fender Deluxe Reverb '65 Reissue, Mono Vertigo Electric Hybrid Gig Bag")

    def test_product_name_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label, 'product name')

    def test_brand_field_label(self):
        product = Products.objects.get(id=1)
        field_label = product._meta.get_field('brand').verbose_name
        self.assertEquals(field_label, 'brand')

    def test_price_name_max_digits(self):
        product = Products.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 7)

    def test_get_absolute_url(self):
        product = Products.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/api/products/1/')

    def test_image_upload_to(self):
        product = Products.objects.get(id=1)
        upload_to = product._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'static/static_dirs/media/')


   # "pk": 1,
   #  "fields": {
   #      "product_name": "Fender Telecaster",
   #      "product_description": "American made, single-coil pickups, Deep-C profile.",
   #      "price": "1546.99",
   #      "inventory": 11,
   #      "brand": "Fender",
   #      "category": "ELECTRIC",
   #      "image": "static/static_dirs/media/Butterscotch_tele.jpg",
   #      "related_products": "Fender Deluxe Reverb '65 Reissue, Mono Vertigo Electric Hybrid Gig Bag"
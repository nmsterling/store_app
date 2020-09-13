from rest_framework import serializers

from .models import Profile, Products, TransactionsHistory, Cart, Reviews

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'address', 'preferred']

# https://stackoverflow.com/questions/35522768/django-serializer-imagefield-to-get-full-url
class ProductsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['id','product_name', 'product_description', 'price', 'inventory', 'image']

    def get_image(self, product):
        request = self.context.get('request')
        image = product.image.url
        return request.build_absolute_uri(image)

class TransactionHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionsHistory
        fields = ['id', 'user', 'product_name', 'quantity_purchased', 'transaction_total', 'timestamp']

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product_name', 'quantity']
        # this specifies the depth of the relationships for related tables and populates those in json
        depth = 2

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'id',
            'user',
            'product_name',
            'review',
            'product_rating',
        ]

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'id',
            'user',
            'product_name',
            'review',
            'product_rating',
        ]
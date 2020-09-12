from rest_framework import serializers

from .models import Profile, Products, TransactionsHistory, Cart

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
    item_total = serializers.SerializerMethodField('get_item_total')
    # sub_total = serializers.SerializerMethodField('get_sub_total')

    def get_item_total(self, cart):
        return cart.product_name.price * cart.quantity

    #     def get_sub_total(self, cart):
    #         sub_total = 0
    #         for user in cart.user:

    #             for product in cart.product_name:
    #                 item_total = product.price * cart.quantity
    #                 sub_total += item_total
    #         return sub_total

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product_name', 'quantity', 'item_total']
        # this specifies the depth of the relationships for related tables and populates those in json
        depth = 2

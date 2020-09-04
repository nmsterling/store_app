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
        fields = ['id','product_name', 'price', 'inventory', 'image']

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
# class Cart(models.Model):
#     user = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=30)
#     quantity = models.IntegerField()

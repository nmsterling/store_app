from django.shortcuts import render

from api.models import Products

# Create your views here.
def list_products(request):
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products
    })
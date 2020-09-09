from django.shortcuts import render

from api.models import Products

# Create your views here.

def list_products(request):
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products
    })

def list_electric(request):
    products = Products.objects.filter(category="Electric Guitar")
    return render(request, 'app/electric.html', {
        "products": products
    })

# create the filtered views...
# def list_acoustic(request):

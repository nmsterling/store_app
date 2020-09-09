from django.shortcuts import render

from api.models import Products

# Create your views here.

# Look up how to put these all into a Class Based APIList View with defs or something

def list_products(request):
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products
    })

def list_electric(request):
    products = Products.objects.filter(category="Electric Guitar")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_acoustic(request):
    products = Products.objects.filter(category="Acoustic")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_amps(request):
    products = Products.objects.filter(category="Amps")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_cases(request):
    products = Products.objects.filter(category="Cases")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

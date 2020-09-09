from django.shortcuts import render
from django.views.generic.list import ListView
from django.db import models

from api.models import Products

# Create your views here.

# Look up how to put these all into a Class Based APIList View with defs or something

def list_products(request):
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products
    })

# class ProductsListView(ListView):
#     model = Products


def list_electric(request):
    products = Products.objects.filter(category="ELECTRIC")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_acoustic(request):
    products = Products.objects.filter(category="ACOUSTIC")
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_amps(request):
    products = Products.objects.filter(category__icontains="AMPS")
    print(products)
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def list_cases(request):
    products = Products.objects.filter(category__icontains="CASES")
    print(products)
    return render(request, 'app/category_filter.html', {
        "products": products
    })

def categories_list_view(request):
    category = str(request.GET.get('category_search')).upper()
    print(category)
    context = Products.objects.filter(category__icontains=category)
    if context:
        return render(request, "app/category_filter.html", {
        "products": context
        })
    return render(request, "app/search_fail.html")
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from api.models import Products, Cart

import itertools
# Create your views here.

def index(request):
    current_user = request.user
    try:
        cart = Cart.objects.get(user=current_user).aggregate('quantity')
        return render(request, 'app/index.html', {
            "cart": cart
        })
    except ObjectDoesNotExist:
        return render(request, 'app/index.html')

# Look up how to put these all into a Class Based APIList View with defs or something

def list_products(request):
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products
    })


def categories_list_view(request):
    category = str(request.GET.get('category_search')).upper()
    print(category)
    context = Products.objects.filter(Q(category__icontains=category) | Q(brand__icontains=category))
    if context:
        return render(request, "app/category_filter.html", {
        "products": context
        })

def categories(request):

    categories = Products.objects.values_list('category', flat=True).distinct()
    if categories:
        return render(request, "app/categories.html", {
            "categories": categories
        })

def filter_products(request, category):
    print(category)
    context = Products.objects.filter(Q(category__icontains=category) | Q(brand__icontains=category))
    print(context)
    if context:
        return render(request, "app/category_filter.html", {
        "products": context
        })
    return render(request, "app/search_fail.html")

def add_to_cart(request):
    if request.method == 'POST':
        data = request.POST.copy()
        product_name = data.get('product_name')
        print(product_name)
        current_user = request.user
        if product_name:
            return render(request, "app/cart.html", {
                "items": product_name,
                "current_user": current_user
            })
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.db.models import Sum

from api.models import Products, Cart

import itertools

# Create your views here.

# Look up how to put these all into a Class Based APIList View with defs or something

def list_products(request):
    # we'll want to call all products regardless if user has cart objects or not
    products = Products.objects.all()
    # check if user is logged in
    if request.user.is_authenticated:
        current_user = request.user
        # call cart objects for current_user
        cart = Cart.objects.filter(user=current_user)
        # if user has objects in their cart proceed
        if cart:
            cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
            # the zeroth index of the below list will be the total items in the user's cart
            cart_list = [int(value) for value in cart_dict.values()]
            return render(request, 'app/products.html', {
                "products": products,
                "cart": cart_list[0]
            })
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
    # query the db for matching queries
    context = Products.objects.filter(Q(category__icontains=category) | Q(brand__icontains=category))
    #if user is authenticated we'll want to provide cart info here too (as in list_products)
    if request.user.is_authenticated:
        current_user = request.user
        cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
        cart_list = [int(value) for value in cart_dict.values()]
        if context:
            return render(request, "app/category_filter.html", {
            "products": context,
            "cart": cart_list[0]
            })
    # user isn't logged in but we still will let them peruse
    if context:
        return render(request, "app/category_filter.html",{
            "products": context
        })
    return render(request, "app/search_fail.html")

def add_to_cart(request, pk):
    current_user = request.user
    product = Products.objects.get(pk=pk)
    # add product to cart
    c = Cart(user=current_user, product_name=product, quantity=1)
    # save to disk
    c.save()
    # get number of items in cart for current user
    cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
    cart_list = [int(value) for value in cart_dict.values()]
    products = Products.objects.all()

    return render(request, "app/products.html", {
        "cart": cart_list[0],
        "products": products
    })

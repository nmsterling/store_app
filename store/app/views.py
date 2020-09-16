from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.db.models import Sum

from api.models import Products, Cart, Reviews

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

def reviews_list(request, pk):
    pk = pk
    product = Products.objects.get(pk=pk)
    print(product.pk)
    reviews = Reviews.objects.filter(product=product.pk)
    if not reviews:
        return render(request, "app/no_reviews.html", {
            "product": product
        })
    return render(request, "app/reviews.html", {
        "product": product,
        "reviews": reviews
    })

def create_review(request, pk):
    current_user = request.user
    print(current_user)
    product = Products.objects.get(pk=pk)
    return render(request, "app/create_review.html", {
        "user": current_user,
        "product": product
    })

def review_save(request):
    if request.method == 'POST':
        current_user = request.user
        print(current_user)
        pk = request.POST.get('pk')
        product = Products.objects.get(pk=pk)
        print(product.product_name)
        review = request.POST.get('review')
        print(review)
        rating = request.POST.get('rating')
        print(rating)
        if current_user and product and review and rating:
            cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
            cart_list = [int(value) for value in cart_dict.values()]
            products = Products.objects.all()
            review = Reviews(user=current_user, product=product, review=review, product_rating=rating)
            review.save()
            return render(request, "app/products.html", {
                "cart": cart_list[0],
                "products": products
            })
        else:
            return HttpResponse('you must fill out all fields to submit review')
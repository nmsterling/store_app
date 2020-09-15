from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.http import HttpResponse

from api.models import Products, Cart, Reviews

import itertools
# Create your views here.

def index(request):
    current_user = request.user
    if current_user:
        try:
            cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
            cart_list = [int(value) for value in cart_dict.values()]
            return render(request, 'app/index.html', {
                "cart": cart_list[0]
            })
        except ObjectDoesNotExist:
            return render(request, 'app/index.html')
    return render(request, 'app/search_fail.html')

# Look up how to put these all into a Class Based APIList View with defs or something

def list_products(request):
    current_user = request.user
    cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
    # shares_dict = Transactions.objects.filter(user=user, title=quote["name"]).aggregate(Sum('shares'))
    # print(shares_dict)
    # shares_list = [int(value) for value in shares_dict.values()]
    # print(shares_list[0])
    # print(shares_list[0] - get_shares)
    cart_list = [int(value) for value in cart_dict.values()]
    products = Products.objects.all()
    return render(request, 'app/products.html', {
        "products": products,
        "cart": cart_list[0]
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
    current_user = request.user
    context = Products.objects.filter(Q(category__icontains=category) | Q(brand__icontains=category))
    cart_dict = Cart.objects.filter(user=current_user).aggregate(Sum('quantity'))
    cart_list = [int(value) for value in cart_dict.values()]
    print(context)
    if context:
        return render(request, "app/category_filter.html", {
        "products": context,
        "cart": cart_list[0]
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
    reviews = Reviews.objects.filter(product_name=product.product_name)
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
            review = Reviews(user=current_user, product_name=product, review=review, product_rating=rating)
            review.save()
            return render(request, "app/products.html", {
                "cart": cart_list[0],
                "products": products
            })
        else:

            return HttpResponse('you must fill out all fields to submit review')

    # < input
    # id = "product_name"
    # type = "hidden"
    # value = "{{ product.product_name }}" >
    # < textarea
    # id = "review"
    # rows = "5"
    # columns = "100"
    # placeholder = "write a review for {{ product.product_name }}" > < / textarea >
    # < label
    # for ="rating" > Give a 1 to 5 star rating < / label >
    # < select
    # id = "rating" >
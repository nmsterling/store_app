from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='app/index.html'), name='index'),
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('shop/', views.list_products, name="list_products"),
    path('cart/', TemplateView.as_view(template_name='app/cart.html'), name='cart'),
    path('search/', views.categories_list_view, name="categories_list_view"),
    path('cart/<int:pk>', views.add_to_cart, name='cart_add'),
    path('filter/<str:category>/', views.filter_products, name="filter"),
    path('reviews/<str:product_name>', views.reviews_list, name="reviews"),
    path('create-review/<str:product_name>/', views.create_review, name='create-review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

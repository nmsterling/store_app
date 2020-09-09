from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from django.views.generic import TemplateView

# app_name = 'app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/index.html'), name='index'),
    path('categories/', TemplateView.as_view(template_name='app/categories.html'), name='categories'),
    path('shop/', views.list_products, name="list_products"),
    # path('shop/', views.ProductsListView.as_view(), name="list_products"),
    path('electric/', views.list_electric, name='electric'),
    path('acoustic/', views.list_acoustic, name='acoustic'),
    path('amps/', views.list_amps, name='amps'),
    path('cases/', views.list_cases, name='cases'),
    path('cart/', TemplateView.as_view(template_name='app/cart.html'), name='cart'),
    path('search/', views.categories_list_view, name="categories_list_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

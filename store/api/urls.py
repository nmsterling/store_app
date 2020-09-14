from django.urls import path

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from api import views

app_name = 'api'

# look up providing template arugument to these views

urlpatterns = [
    path('profile/', views.ProfileListCreate.as_view()),
    path('products/', views.ProductsListCreate.as_view()),
    path('transactions/', views.TransactionHistoryListCreate.as_view()),
    path('cart/', views.CartListCreate.as_view(), name='cart'),
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='update-cart'),
    path('reviews/<str:product_name>', views.ReviewsList.as_view(), name='reviews'),
    path('create-review/<str:product_name>/', views.ReviewsCreate.as_view(), name='create-review'),
    path('totals/', views.totals, name="totals"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


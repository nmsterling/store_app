from django.urls import path

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from api import views

app_name = 'api'

urlpatterns = [
    path('profile/', views.ProfileListCreate.as_view()),
    path('products/', views.ProductsListCreate.as_view()),
    path('transactions/', views.TransactionHistoryListCreate.as_view()),
    path('cart/', views.CartListCreate.as_view(), name='cart'),
    path('cart/<int:pk>/', views.CartDetail.as_view(), name='update-cart'),
    path('totals/', views.totals, name="totals"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


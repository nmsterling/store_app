from django.urls import path
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/index.html', name='index'))
]
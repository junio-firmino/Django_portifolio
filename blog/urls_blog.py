from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.metodo_views_blog),
]
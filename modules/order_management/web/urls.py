from django.urls import path

from modules.order_management.web import views

urlpatterns = [
    path('', views.index, name='index'),
]
from ..web import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"transactions", views.TransactionViewSet)

router.register(r"shipping_order", views.ShippingOrderViewSet)

router.register(r"purchase_order", views.PurchaseOrderViewSet)

router.register(r"item_instance", views.ItemViewSet)

urlpatterns = router.urls

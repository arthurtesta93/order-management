
from ..web import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"transactions", views.TransactionViewSet)
router.register(r"purchase_order", views.PurchaseOrderViewSet)
router.register(r"item_instance", views.ItemViewSet)
router.register(r"shipping_order", views.ShippingOrderViewSet)

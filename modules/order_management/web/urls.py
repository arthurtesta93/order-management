
from ..web import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"-purchase_order", views.PurchaseOrderViewSet)
router.register(r"-item", views.ItemViewSet)
router.register(r"-shipping_order", views.ShippingOrderViewSet)

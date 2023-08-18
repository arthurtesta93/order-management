from ..web import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"transactions", views.TransactionViewSet)

router.register(r"shipping_order", views.ShippingOrderViewSet)

router.register(r"shipping_order_list_purchase_orders", views.ShippingOrderPurchaseOrdersViewSet)

router.register(r"purchase_order", views.PurchaseOrderViewSet)

router.register(r"purchase_order_list_items", views.PurchaseOrderItemsViewSet)

router.register(r"item_instance", views.ItemViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('transactions/', views.TransactionViewSet.as_view({'get': 'list'})),
#     path('transactions/<int:pk>/', views.TransactionViewSet.as_view({'get': 'retrieve'})),
#     path('shipping_order/', views.ShippingOrderViewSet.as_view({'get': 'list'})),
#     path('shipping_order/<int:pk>/', views.ShippingOrderViewSet.as_view({'get': 'retrieve'})),
#     path('shipping_order_list_purchase_orders/', views.ShippingOrderPurchaseOrdersViewSet.as_view({'get': 'list'})),
#     path('shipping_order_list_purchase_orders/<int:pk>/', views.ShippingOrderPurchaseOrdersViewSet.as_view({'get': 'retrieve'})),
#     path('purchase_order/', views.PurchaseOrderViewSet.as_view({'get': 'list'})),
#     path('purchase_order/<int:pk>/', views.PurchaseOrderViewSet.as_view({'get': 'retrieve'})),
#     path('purchase_order_list_items/', views.PurchaseOrderItemsViewSet.as_view({'get': 'list'})),
#     path('purchase_order_list_items/<int:pk>/', views.PurchaseOrderItemsViewSet.as_view({'get': 'retrieve'})),

from rest_framework import routers

from ..web import views

router = routers.DefaultRouter()
router.register(r"transactions", views.TransactionViewSet)
router.register(r"organizations", views.OrganizationViewSet)

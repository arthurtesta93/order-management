from rest_framework import routers

from ..web import views

router = routers.DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet)
router.register(r"facilities", views.FacilityViewSet)
router.register(r"items", views.ItemViewSet)
router.register(r"corporate_offices", views.CorporateOfficeViewSet)
router.register(r"warehouses", views.WarehouseViewSet)
router.register(r"storages", views.StorageViewSet)
router.register(r"dock", views.DockViewSet)
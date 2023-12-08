from rest_framework import routers

from ..web import views


router = routers.DefaultRouter()
router.register(r"contacts", views.ContactViewSet, basename='contact')
router.register(r"organizations", views.OrganizationViewSet)
router.register(r"facilities", views.FacilityViewSet, basename='facility')
router.register(r"items", views.ItemViewSet)
router.register(r"corporate_offices", views.CorporateOfficeViewSet)
router.register(r"warehouses", views.WarehouseViewSet)
router.register(r"dock", views.DockViewSet)


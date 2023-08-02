from rest_framework import routers

from ..web import views

router = routers.DefaultRouter()
router.register(r"contacts", views.ContactViewSet, basename='contact')
router.register(r"contacts/search", views.ContactSearchViewSet, basename='contact')
router.register(r"contacts/search_by_organization", views.ContactSearchByOrganizationViewSet, basename='contact')
router.register(r"organizations", views.OrganizationViewSet)
router.register(r"facilities", views.FacilityViewSet)
router.register(r"facilities/search_zip_code", views.FacilitySearchByZipCodeViewSet)
router.register(r"facilities/search_by_organization", views.FacilitySearchByOrganizationViewSet)
router.register(r"items", views.ItemViewSet)
router.register(r"corporate_offices", views.CorporateOfficeViewSet)
router.register(r"warehouses", views.WarehouseViewSet)
router.register(r"dock", views.DockViewSet)
router.register(r"dock/search_by_warehouse", views.DockSearchByWarehouseViewSet)

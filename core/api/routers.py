from rest_framework.routers import DefaultRouter

from core.api.views import ClientViewSet

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')

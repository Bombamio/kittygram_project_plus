from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)


urlpatterns = router.urls

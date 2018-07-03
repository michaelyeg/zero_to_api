from django.conf.urls import url
from rest_framework import routers
from sportCars.views import sportsCarViewSet

router = routers.DefaultRouter()
router.register(r'sportCars', sportsCarViewSet)

urlpatterns = router.urls
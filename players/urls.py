from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, ClubViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'clubs', ClubViewSet, basename='club')

urlpatterns = router.urls
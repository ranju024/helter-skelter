from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, CommentViewSet

router = DefaultRouter()

router.register("reviews", ReviewViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls
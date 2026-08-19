from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, CommentViewSet, RatingViewSet

router = DefaultRouter()

router.register("ratings", RatingViewSet)
router.register("reviews", ReviewViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls
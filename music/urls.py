from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, AlbumViewSet, SongViewSet, GenreViewSet

router = DefaultRouter()

router.register('artists', ArtistViewSet)
router.register('albums', AlbumViewSet)
router.register('songs', SongViewSet)
router.register('genres', GenreViewSet)

urlpatterns = router.urls
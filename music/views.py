from rest_framework import viewsets

from .models import Artist, Album, Song, Genre
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    SongSerializer,
    GenreSerializer,
)
from .permissions import IsAdminOrReadOnly

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAdminOrReadOnly]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminOrReadOnly]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer  
    permission_classes = [IsAdminOrReadOnly]

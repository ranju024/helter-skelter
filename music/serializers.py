from rest_framework import serializers
from .models import Artist, Album, Song, Genre


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'slug', 'bio', 'country', 'formed_date', 'is_band', 'members', 'is_verified']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'slug', 'artist', 'cover_image', 'description', 'release_date', 'album_type', 'genre']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'slug', 'album', 'artists', 'genre', 'description', 'duration', 'track_number', 'audio_file', 'cover_image', 'release_date']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']

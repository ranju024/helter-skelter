from django.db import models

class Artist(models.Model):
    # name, slug, bio, image, country, formed_date, is_band, members, is_verified, created_at, updated_at
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=200)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    formed_date = models.DateField(blank=True, null=True)
    is_band = models.BooleanField(default=False)
    members = models.ManyToManyField('self', blank=True, symmetrical=False) #since django makes M2M fields symmetrical by default
    is_verified = models.BooleanField(default=False) # if artist is admin verified
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Artist {self.name}"




class Album(models.Model):
    # title, slug, artist (ForeignKey Artist), cover_image, description, release_date, album_type (choices), 
    # genre (M2M with Genre model), created_at, updated_at
    ALBUM_TYPE_CHOICES = [
        ('LP', 'LP'), # Long Play ( 8+ songs)
        ('EP', 'EP'), # Extended Play (4-6 songs)
        ('SINGLE', 'Single'), # only one song
        ('COMPILATION', 'Compilation'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover_image = models.ImageField(upload_to='albums/', blank=True, null=True)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    album_type = models.CharField(max_length=20, choices=ALBUM_TYPE_CHOICES, default='SINGLE')
    genre = models.ManyToManyField('Genre', blank=True, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"





class Song(models.Model):
    # title, slug, album ( ForeignKey Album), artists (M2M Artist),
    # genre (M2M Genre), description, duration (DurationField), track_number ( if the song belongs to an album, null otherwise), 
    # audio_file(FileField), cover_image, release_date, created_at, updated_at
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)
    artists = models.ManyToManyField(Artist, related_name='songs')
    genre = models.ManyToManyField('Genre', blank=True, related_name='songs')
    description = models.TextField(null=True, blank=True)  #musicopedia
    duration = models.DurationField(blank=True, null=True)
    track_number = models.PositiveIntegerField(blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='songs/covers/', null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Song {self.title}"






class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Genre {self.name}"
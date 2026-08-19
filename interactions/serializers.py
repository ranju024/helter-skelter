from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from .models import Review, Comment, Rating
from music.models import Album, Artist, Song

# only these levels can be rated/reviewed/commented on
ALLOWED_MODELS = (Album, Artist, Song)

def check_content_type(content_type):
    model_class = content_type.model_class()
    if model_class not in ALLOWED_MODELS:
        raise serializers.ValidationError(f"Content type must be one of: {ALLOWED_MODELS}")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'content_type', 'object_id', 'score', 'created_at', 'updated_at']
        read_only_fields = ['user']

    def validate_content_type(self, value):
        check_content_type(value)
        return value
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'content_type', 'object_id', 'title', 'body', 'created_at', 'updated_at']
        read_only_fields = ['user']

    def validate_content_type(self, value):
        check_content_type(value)
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content_type', 'object_id', 'body', 'parent', 'created_at', 'updated_at']
        read_only_fields = ['user']

    def validate_content_type(self, value):
        check_content_type(value)
        return value

from rest_framework import serializers
from .models import FavoriteGist


class GistFileSerializer(serializers.Serializer):
    """
    Simple serializer to parse gist API gist file object
    """
    gist_id = serializers.CharField()
    file_name = serializers.CharField()
    favorite = serializers.BooleanField(default=False)


class GistSerializer(serializers.Serializer):
    """
    Simple serializer to parse gist API gist object
    """
    gist_id = serializers.CharField()
    github_user = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    files = GistFileSerializer(many=True)
    favorite = serializers.BooleanField(default=False)


class FavoriteGistSerializer(serializers.ModelSerializer):
    """
    Serializer for the FavoriteGist Model
    """
    model = FavoriteGist

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FavoriteGist, FavoriteGistFile
from .services import get_all_by_username, get_gist_by_id
from .serializers import GistSerializer


@api_view(['GET'])
def by_username(request, username: str) -> Response:
    """
    Get all gists for a given username
    :param request:
    :param username:
    :return:
    """
    gists = get_all_by_username(username)
    # Get a flat list of favorite IDs to compare to retrieved gists
    favorites = FavoriteGist.objects.values('gist_id')
    for gist in gists:
        # If the gist_id is in the favorites then flip the favorite
        gist.favorite = gist.gist_id in favorites
    serializer = GistSerializer(gists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def by_id(request, gist_id: str) -> Response:
    """
    Get a gist's details by ID
    :param request:
    :param gist_id:
    :return:
    """
    gist = get_gist_by_id(gist_id)
    # If there's an object in the Db with the gist_id then assume it's favorited
    gist.favorite = FavoriteGist.objects.filter(gist_id=gist_id).exists()
    serializer = GistSerializer(gist)
    return Response(serializer.data)


@api_view(['GET'])
def favorites(request) -> Response:
    """
    Get list of all favorited gists
    :param request:
    :return:
    """
    return Response()


@api_view(['POST'])
def favorite_gist(request, gist_id: str) -> Response:
    """
    Favorite a gist and store that in the database
    :param request:
    :param gist_id:
    :return:
    """
    return Response()


@api_view(['DELETE'])
def unfavorite_gist(request, gist_id: str) -> Response:
    """
    Unfavorite a gist
    :param request:
    :param gist_id:
    :return:
    """
    return Response()


@api_view(['POST'])
def favorite_gist_file(request, gist_id: str, file_name: str) -> Response:
    """
    Favorite a gist file
    :param request:
    :param gist_id:
    :param file_name:
    :return:
    """
    return Response()


@api_view(['DELETE'])
def unfavorite_gist_file(request, gist_id: str, file_name: str) -> Response:
    """
    Remove gist file from favorites
    :param request:
    :param gist_id:
    :param file_name:
    :return:
    """
    return Response()

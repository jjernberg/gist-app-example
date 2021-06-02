from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FavoriteGist, FavoriteGistFile
from .services import get_all_by_username, get_gist_by_id


@api_view(['GET'])
def by_username(request, username: str) -> Response:
    """
    Get all gists for a given username
    :param request:
    :param username:
    :return:
    """
    return Response()


@api_view(['GET'])
def by_id(request, gist_id: str) -> Response:
    """
    Get a gist's details by ID
    :param request:
    :param gist_id:
    :return:
    """
    return Response()


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

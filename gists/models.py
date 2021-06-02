from django.db import models


class FavoriteGist(models.Model):
    """
    Gists saved to track favorites.   If it exists then it's a favorite.  Also including some fields that will
    be nice to have in a list.
    """
    gist_id = models.CharField(max_length=30)  # Seems like they are 20 chars, but adding wiggle room
    git_username = models.CharField(max_length=120)
    description = models.TextField()


class FavoriteGistFile(models.Model):
    """
    Files related to a Gist to keep track of favorite.   If it exists then it's a favorite.

    Note:  Looked like this is a bonus in the requirements but going to stub it out either way.
    """
    gist_id = models.CharField(max_length=30)  # Seems like they are 20 chars, but adding wiggle room
    file_key = models.CharField(max_length=512)  # This looks to be the file name

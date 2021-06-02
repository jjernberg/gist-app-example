from typing import Iterable, Optional
import pendulum


class GistFile:
    """
    Class for files related to a Gist
    """
    def __init__(self, gist_id: str, file_name: str, favorite: bool = False):

        self.gist_id = gist_id
        self.file_name = file_name
        self.favorite = favorite  # Not retrieved by the API but will be used as a flag to mark favorites


class Gist:

    def __init__(self, gist_id: str, github_user: str, description: str, created_at: pendulum.DateTime,
                 files: Optional[Iterable[GistFile]] = None, favorite: bool = False):

        if not files:
            files = []

        self.gist_id = gist_id
        self.github_user = github_user
        self.description = description
        self.created_at = created_at
        self.files = files
        self.favorite = favorite  # Not retrieved by the API but will be used as a flag to mark favorites



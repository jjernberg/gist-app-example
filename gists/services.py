from typing import Iterable, Optional, List
import pendulum
import requests


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


def _setup_gist_from_data(data) -> Gist:
    """
    Setup a Gist object from the known response data
    :param data:
    :return:
    """
    gist_id = data.get('id')
    files_data = data.get('files')  # This is oddly an object, so going to make it a list of file names
    files_list = []
    if files_data:
        files_list = list(files_data.keys())
        files_list = [GistFile(gist_id=data.get('id'), file_name=file_name) for file_name in files_list]
    return Gist(
        gist_id=gist_id,
        github_user=data.get('owner', {}).get('login'),
        description=data.get('description'),
        created_at=pendulum.parse(data.get('created_at')),
        files=files_list
    )


def get_all_by_username(username: str) -> Iterable[Gist]:
    """
    Get all public gists for a user
    :param username:
    :return:
    """
    try:
        # Going to set per_page to 100 but shoud likely deal with pagination
        result = requests.get(f'https://api.github.com/users/{username}/gists?per_page=100')
        result.raise_for_status()
        data = result.json()
        gists: List[Gist] = []
        # Loop through returned gists to setup a List of Gist objects
        for gist in data:
            gists.append(_setup_gist_from_data(data))
        return gists
    except Exception:
        # Going to swallow up errors for now and just return an empty list as if they had none
        return []



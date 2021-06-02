# Gists App


## Django API and gist API service

The API and service to retrieve the gists took about an hour to develop.

The `gists` direction/app contains the API functionality for the challenge.   

* views.py - Provides the endpoints
* services.py - This is the requested library/service to handle interactions with the gist API
* models.py - The DB models to store the favorites
* serializers.py - The serializers to provide the structure for the response data

### Build Instructions

(Recommended) A basic Dockerfile is provided.   You can run the API using docker with commands similar to...

```
docker build -t gist-django-api .
docker run --name gist-django-api -p 8000:8000 -d gist-django-app
```

You can also run this locally using a virtualenv if you have python3 installed...

```
python3 -m venv venv
source venv/bin/active
pip install -r requirements.txt
python manage.py runserver
```
# Gists App

To combine this into one package the structure is a different from what I would usually set up.   I placed the front-end
in `gists-fe` and the API is in the root.

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

## React Front-end

I spent about an hour getting the front-end to this point.  I had to make the choice to stick to Angular which I've used
more recently or use React.   Angular can take 30 minutes just to get going, so I chose React and had to refresh a bit of
knowledge.  I'm fairly confident I could have finished with 30 more minutes. 

I brought it to the point of being able to search by username and have a decent looking list of gists and started 
adding the pieces needed to favorite a Gist.

### Build instructions

```
cd gists-fe
npm install
npm start
```

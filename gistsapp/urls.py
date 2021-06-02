from django.urls import path, include

urlpatterns = [
    path('gists/', include('gists.urls')),
]

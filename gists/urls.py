from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import gists.views as views

urlpatterns = [
    path('by_username/<str:username>/', views.by_username),
    path('by_id/<str:gist_id>/', views.by_id),
    path('favorite/<str:gist_id>/', views.favorite_gist),
    path('unfavorite/<str:gist_id>/', views.unfavorite_gist),
]

urlpatterns = format_suffix_patterns(urlpatterns)
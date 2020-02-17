from django.urls import path
from ghibliapp.views import MoviesListView

urlpatterns = [
    path('movies', MoviesListView.movies_list, name='movies_list'),
]

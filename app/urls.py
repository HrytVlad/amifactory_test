from django.urls import path

from app.views import GenresListView, MovieDetailView, MoviesListView

urlpatterns = [
    path("genres/", GenresListView.as_view(), name='genre'),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name='movie_detail'),
    path("movies/", MoviesListView.as_view(), name='movie_list'),
               ]


app_name = "app"

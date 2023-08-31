from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, Paginator
from django.http import JsonResponse
from django.views import generic, View

from app.models import Genre, Movie


def convert_data(movie: Movie) -> dict:
    return {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "release_year": movie.release_year,
        "mpa_rating": movie.mpa_ratings,
        "imdb_rating": float(movie.imdb_rating),
        "duration": movie.duration,
        "poster": movie.poster.url,
        "bg_picture": movie.bg_picture.url,
        "genres": list(movie.genres.values("id", "title")),
        "directors": list(movie.directors.values("id", "first_name", "last_name")),
        "writers": list(movie.writers.values("id", "first_name", "last_name")),
        "stars": list(movie.stars.values("id", "first_name", "last_name")),
    }


class GenresListView(generic.ListView):
    model = Genre

    def get(self, request, pk=None, *args, **kwargs):
        data = list(self.model.objects.values("id", "title"))
        return JsonResponse(data, safe=False)


class MovieDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        try:
            movie = Movie.objects.get(pk=pk)
            movie_dict = convert_data(movie)
            return JsonResponse(movie_dict, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"error": ["movie__not_found"]}, status=404)


class MoviesListView(View):

    def get(self, request, *args, **kwargs):
        genre_id = request.GET.get("genre")
        src = request.GET.get("src")
        page = request.GET.get("page")

        queryset = Movie.objects.all()
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)

            if not queryset.exists():
                return JsonResponse({"error": ["genre__invalid"]}, status=404)

        if src and 2 <= len(src) <= 20:
            queryset = queryset.filter(title__istartswith=src)

        paginator = Paginator(queryset, 5)
        try:
            movies = paginator.page(page)
        except EmptyPage:
            return JsonResponse({"error": ["page__out_of_bounds"]}, status=404)

        movie_dicts = [convert_data(movie) for movie in movies]

        response_data = {
            "pages": paginator.num_pages,
            "total": len(movie_dicts),
            "results": movie_dicts,
        }
        return JsonResponse(response_data)

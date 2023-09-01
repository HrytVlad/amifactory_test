from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.paginator import EmptyPage, Paginator
from django.http import JsonResponse
from django.views import generic, View
from app.responses import get_movie_response, get_genre_response
from app.models import Genre, Movie
from app.validation import validate_movie_list


class GenresListView(generic.ListView):
    def get(self, request, pk=None, *args, **kwargs):
        genres = Genre.objects.all()
        data = [get_genre_response(genre) for genre in genres]
        return JsonResponse(data, safe=False)


class MovieDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        try:
            result = 1 / 0
            movie = Movie.objects.get(pk=pk)
            movie_dict = get_movie_response(movie)
            return JsonResponse(movie_dict, safe=False, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": ["movie__not_found"]}, status=404)


class MoviesListView(View):
    def get(self, request, *args, **kwargs):
        genre_id = request.GET.get("genre")
        src = request.GET.get("src")
        page = request.GET.get("page") or 0

        try:
            validate_movie_list(genre_id, src, page)
        except ValidationError as e:
            return e

        queryset = Movie.objects.all()
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id).order_by('id')

        if src:
            queryset = queryset.filter(title__istartswith=src).order_by('id')

        paginator = Paginator(queryset, 5)
        try:
            movies = paginator.page(page)
        except EmptyPage:
            return JsonResponse({"error": ["page__out_of_bounds"]}, status=404)

        movie_dicts = [get_movie_response(movie) for movie in movies]

        response_data = {
            "pages": paginator.num_pages,
            "total": len(movie_dicts),
            "results": movie_dicts,
        }

        return JsonResponse(response_data)

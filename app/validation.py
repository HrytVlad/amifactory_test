from django.core.exceptions import ObjectDoesNotExist, BadRequest
from django.http import JsonResponse

from app.models import Genre


def movie_list_validator(genre_id=None, src=None, page=None):
    if genre_id:
        try:
            Genre.objects.get(pk=genre_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": ["genre__invalid"]}, status=400)

    if src and 2 > len(src) >= 20:
        return JsonResponse({"error": ["src__invalid"]}, status=400)

    if page and not page.isdigit() or int(page) < 0:
        return JsonResponse({"error": ["page__invalid"]})

    return None

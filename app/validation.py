from django.core.exceptions import ObjectDoesNotExist, BadRequest, ValidationError
from app.models import Genre


def validate_movie_list(genre_id=None, src=None, page=None):
    if genre_id:
        try:
            Genre.objects.get(pk=genre_id)
        except ObjectDoesNotExist:
            raise ValidationError({"error": ["genre__invalid"]})

    if src and 2 > len(src) >= 20:
        raise ValidationError({"error": ["src__invalid"]})

    if page and not page.isdigit() or int(page) < 0:
        raise ValidationError({"error": ["page__invalid"]})

from app.models import Genre, Movie


def get_genre_response(genre: Genre) -> dict:
    return {
        "id": genre.id,
        "title": genre.title,
    }


def get_movie_response(movie: Movie) -> dict:

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
        "genres": [get_genre_response(genre) for genre in movie.genres.all()],
        "directors": list(movie.directors.values("id", "first_name", "last_name")),
        "writers": list(movie.writers.values("id", "first_name", "last_name")),
        "stars": list(movie.stars.values("id", "first_name", "last_name")),
    }

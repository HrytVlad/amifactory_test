from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CreationTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Genre(CreationTime):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Person(CreationTime):
    SPECIALIST_CHOICES = (
        ("D", "director"),
        ("W", "writer"),
        ("A", "actor"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    types = models.CharField(max_length=1, choices=SPECIALIST_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.types}"


class Movie(CreationTime):
    RATING_CHOICES = (
        ("G", "General Audiences"),
        ("PG", "Parental Guidance"),
        ("PG-13", "Parents Strongly Cautioned"),
        ("R", "Restricted"),
        ("NC-17", "Adults Only"),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    poster = models.ImageField(upload_to="poster")
    bg_picture = models.ImageField(upload_to="bg_poster")
    release_year = models.IntegerField()
    mpa_ratings = models.CharField(max_length=5, choices=RATING_CHOICES)
    imdb_rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    directors = models.ManyToManyField(Person, related_name="movie_directors")
    writers = models.ManyToManyField(Person, related_name="movie_writers")
    stars = models.ManyToManyField(Person, related_name="movie_stars")

    def __str__(self):
        return (
            f"{self.title} "
            f"imdb rating: {self.imdb_rating} "
            f"duration: {self.duration}"
        )

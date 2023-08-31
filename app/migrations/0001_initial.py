# Generated by Django 4.2.4 on 2023-08-31 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "types",
                    models.CharField(
                        choices=[("D", "director"), ("W", "writer"), ("A", "actor")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=5000)),
                ("poster", models.ImageField(upload_to="poster")),
                ("bg_picture", models.ImageField(upload_to="bg_poster")),
                ("release_year", models.IntegerField()),
                (
                    "mpa_ratings",
                    models.CharField(
                        choices=[
                            ("G", "General Audiences"),
                            ("PG", "Parental Guidance"),
                            ("PG-13", "Parents Strongly Cautioned"),
                            ("R", "Restricted"),
                            ("NC-17", "Adults Only"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "imdb_rating",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("duration", models.IntegerField()),
                (
                    "directors",
                    models.ManyToManyField(
                        related_name="movie_directors", to="app.person"
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(related_name="movie_genres", to="app.genre"),
                ),
                (
                    "stars",
                    models.ManyToManyField(related_name="movie_stars", to="app.person"),
                ),
                (
                    "writers",
                    models.ManyToManyField(
                        related_name="movie_writers", to="app.person"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

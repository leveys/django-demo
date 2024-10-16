from django.db import models


class Movie(models.Model):
    adult = models.BooleanField()
    belongs_to_collection = models.JSONField()
    budget = models.IntegerField()
    genres = models.JSONField(default=list)
    homepage = models.URLField()
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=10)
    original_language = models.CharField(max_length=2)
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField(default=0)
    poster_path = models.TextField()
    production_companies = models.JSONField()
    production_countries = models.JSONField()
    release_date = models.DateField(null=True)
    revenue = models.BigIntegerField(default=0)
    runtime = models.FloatField(default=0)
    spoken_languages = models.JSONField()
    status = models.CharField(max_length=20)
    tagline = models.TextField(blank=True)
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    keywords = models.JSONField(null=True)

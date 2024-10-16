from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'url', 
            'adult', 
            'belongs_to_collection', 
            'budget', 
            'genres', 
            'homepage', 
            'id', 
            'imdb_id', 
            'original_language', 
            'original_title', 
            'overview', 
            'popularity', 
            'poster_path', 
            'production_companies', 
            'production_countries', 
            'release_date', 
            'revenue', 
            'runtime', 
            'spoken_languages', 
            'status', 
            'tagline', 
            'title', 
            'video', 
            'vote_average', 
            'vote_count', 
            'keywords'
        ]

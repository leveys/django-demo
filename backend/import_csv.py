import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo.settings')

import django
django.setup()

import csv
from app.models import Movie


def import_movies(file_path, max_rows = 50000):
    existing_movies = set(Movie.objects.values_list('id', flat=True))

    batch_size = 1000
    movies_to_create = []
    rows_added = 0
    i = 0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_id = row['new_id']
            if int(movie_id) not in existing_movies:
                movie = Movie(
                    adult = row['adult'],
                    belongs_to_collection = row['belongs_to_collection'],
                    budget = row['budget'],
                    genres = row['genres'],
                    homepage = row['homepage'][:200],
                    id = movie_id,
                    imdb_id = row['imdb_id'],
                    original_language = row['original_language'],
                    original_title = row['original_title'],
                    overview = row['overview'],
                    popularity = float(row['popularity'].strip() or 0),
                    poster_path = row['poster_path'],
                    production_companies = row['production_companies'],
                    production_countries = row['production_countries'],
                    release_date = row['release_date'] if row['release_date'] != '' else None,
                    revenue = int(row['revenue'].strip() or 0),
                    runtime = float(row['runtime'].strip() or 0),
                    spoken_languages = row['spoken_languages'],
                    status = row['status'],
                    tagline = row['tagline'],
                    title = row['title'],
                    video = row['video'],
                    vote_average = float(row['vote_average'].strip() or 0),
                    vote_count = int(row['vote_count'].strip() or 0),
                    keywords = row['keywords']
                )
                rows_added += 1
                movies_to_create.append(movie)
                existing_movies.add(int(movie_id))
                if len(movies_to_create) >= batch_size:
                    Movie.objects.bulk_create(movies_to_create)
                    movies_to_create = []
            i += 1
            if i >= max_rows:
                break
        if movies_to_create:
            Movie.objects.bulk_create(movies_to_create)
    return rows_added

if __name__ == '__main__':

    print('importing movies...')
    rows_added = import_movies('data/db/movies_small.csv')
    print(f'{rows_added} movies added')


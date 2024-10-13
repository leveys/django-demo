from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['title', 'keywords']
    ordering_fields = ['id', 'title']

from django_filters.rest_framework import DjangoFilterBackend
from .models import (UserProfile, Director, Actor, Movie,MovieLanguages,
                 Genre, Rating, Country, Moments, FavoriteMovie, Favorite, History)
from .serializers import (UserProfileSerializer, DirectorSerializer, DirectorDetailSerializer, ActorSerializer,ActorDetailSerializer,
                          MovieLanguagesSerializer,MovieListSerializer, MovieDetailSerializer, MomentsSerializer,
                          GenreSerializer, GenreDetailSerializer,CountrySerializer,CountryDetailSerializer , FavoriteSerializer, RatingSerializer, HistorySerializer
                          , FavoriteMovieSerializer)
from rest_framework import viewsets, generics, permissions
from .filters import MovieFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import MoviePagination
from .permissions import CheckStatus, RatingPermission



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)



class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MoviePagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [CheckStatus]

class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [RatingPermission]

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer



class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer

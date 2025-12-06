from django.urls import include, path
from rest_framework import routers
from .views import (UserProfileViewSet, DirectorListAPIView, DirectorDetailAPIView, ActorListAPIView,
                    ActorDetailSerializer, MovieListAPIView, MovieDetailAPIView,
                    MovieLanguagesViewSet,
                    GenreListAPIView,GenreDetailAPIView, RatingViewSet, CountryListAPIView, CountryDetailAPIView, MomentsViewSet,
                    FavoriteMovieViewSet, FavoriteViewSet,
                    HistoryViewSet, MovieDetailAPIView, ActorDetailAPIView)


router = routers.SimpleRouter()
router.register('userprofile', UserProfileViewSet)
router.register('movielanguages', MovieLanguagesViewSet)
router.register('rating', RatingViewSet)
router.register('moments', MomentsViewSet)
router.register('favoritemovie', FavoriteMovieViewSet)
router.register('favorite', FavoriteViewSet)
router.register('history', HistoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('country/', CountryListAPIView.as_view(), name='country-list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('director/', DirectorListAPIView.as_view(), name='director-list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor-list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre-list'),
    path('genre/', GenreDetailAPIView.as_view(), name='genre-detail'),

]

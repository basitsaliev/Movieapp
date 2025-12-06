from rest_framework import serializers
from .models import (UserProfile, Director, Actor, Movie,MovieLanguages,
                 Genre, Rating, Country, Moments, FavoriteMovie, Favorite, History)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']

class UserProfileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields =['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']





class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [ 'country_name']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [ 'genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name',
                  'year', 'country', 'genre']

class GenreDetailSerializer(serializers.ModelSerializer):
    genre = MovieListSerializer
    class Meta:
        model = Genre
        fields = ['genre_name' , 'genre']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor = MovieListSerializer
    class Meta:
        model = Actor
        fields = ['actor_name',  'bio','age' , 'actor_image','actor']


class DirectorDetailSerializer(serializers.ModelSerializer):
    director = MovieListSerializer(many=True, read_only=True)
    age = serializers.DateField(format='%Y-%d')
    class Meta:
        model = Director
        fields =['director_name', 'bio','age' , 'director_image', 'director']

class CountryDetailSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name',  'movies']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']

class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileRatingSerializer()
    created_date = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Rating
        fields = [ 'user', 'stars',  'parent','stars', 'text', 'created_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    moments = MomentsSerializer(many=True, read_only=True)
    movie_languages = MovieLanguagesSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [ 'movie_name', 'year', 'country', 'director',
                   'actor', 'genre','types', 'movie_time', 'description',
                   'movie_trailer' , 'movie_image', 'moments', 'movie_languages', 'ratings', 'get_avg_rating', 'get_count_people', 'status_movie']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_color_people()

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'






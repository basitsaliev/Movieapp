from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simle', 'simle'),
)

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(18),
                                                  MaxValueValidator(80)],
                                      null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    status = models.CharField(choices=STATUS_CHOICES, default='simle')
    avatar = models.ImageField(upload_to='user_avatars/',null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
   country_name = models.CharField(max_length=64, unique=True)

   def __str__(self):
        return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=64)
    bio = models.TextField()
    age = models.DateField()
    director_image = models.ImageField(upload_to="Director_images/")

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    bio = models.TextField()
    age = models.DateField()
    actor_image = models.ImageField(upload_to="Actor_images/")
    def __str__(self):
        return self.actor_name



class Genre(models.Model):
    genre_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ManyToManyField(Country, related_name='movies')
    director = models.ManyToManyField(Director, related_name='director')
    actor = models.ManyToManyField(Actor, related_name='actor')
    genre = models.ManyToManyField(Genre, related_name='genre')
    TYPE_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = models.CharField(choices=TYPE_CHOICES)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to="Movie_images/")
    status_movie = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name

    def get_avg_rating(self):
        color = self.cratings.all()
        if color.exists():
           return round(sum([i.stars for i in color]) / color.count(), 2)
        return 0


    def get_count_people(self):
        return self.cratings.count()

class MovieLanguages(models.Model):
    language = models.CharField(max_length=64)
    video = models.FileField(upload_to="Movie_videos/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_languages')

    def __str__(self):
        return f'{self.movie}, {self.language}'



class Moments(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='moments')
  movie_moments = models.ImageField(upload_to="Moment_videos/")

  def __str__(self):
      return f'{self.movie}'




class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='cratings')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    text  = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class FavoriteMovie(models.Model):
    favorite_movie = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class History(models.Model):
    user= models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'


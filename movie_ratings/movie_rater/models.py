from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 50)
    release_date = models.CharField(max_length = 50)
    video_release = models.CharField(max_length = 40)
    url = models.CharField(max_length = 150)
    unknown = models.CharField(max_length = 50)
    action_genre = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length = 1)
    occupation = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 40)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 50)
    release_date = models.CharField(max_length = 50)
    video_release = models.CharField(max_length = 40)
    url = models.CharField(max_length = 150)
    unknown = models.CharField(max_length = 50)
    action_genre = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

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

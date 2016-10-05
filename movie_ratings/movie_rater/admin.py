from django.contrib import admin

from movie_rater.models import Rater, Movie, Rating
# Register your models here.
admin.site.register([Rater, Movie, Rating])

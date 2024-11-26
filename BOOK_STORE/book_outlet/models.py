from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)   # The max_length argument is must to pass to CharField constructor
    rating = models.IntegerField()
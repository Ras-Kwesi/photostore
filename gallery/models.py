from django.db import models

# Create your models here.



class Location(models.Model):
    location = models.CharField(max_length=30)


class Category(models.Model):
    category = models.CharField(max_length=20)


class Image(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    categorykey = models.ForeignKey(Category)
    locationkey = models.ForeignKey(Location)
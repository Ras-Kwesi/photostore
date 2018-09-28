from django.db import models

# Create your models here.



class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Image(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    categorykey = models.ForeignKey(Category)
    locationkey = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def saveImage(self):
        self.save()


    def deleteImage(self):
        self.delete()

    # @classmethod
    # def getImage(cls):

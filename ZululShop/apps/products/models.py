from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    vegetables = 'vegetables'
    fruits = 'fruits'
    something_unusual = 'something unusual'
    CHOICES = (
        (vegetables, 'vegetables'), 
        (fruits, 'fruits'), 
        (something_unusual, 'something unusual'), 
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    seller = models.ForeignKey(User, related_name = 'seller', blank = True, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    image = models.URLField(max_length=200, blank=True)
    amount = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=25 ,choices=CHOICES)

    def __str__(self):
        return self.name




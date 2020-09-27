from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    avatar = models.URLField(max_length=300)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.username



    
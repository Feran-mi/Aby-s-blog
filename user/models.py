from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user_name = models.OneToOneField( User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(default= 'defaul.jpg', upload_to= 'profile_pics/')

    def __str__ (self): 
     return f'{self.user_name.username} profile_pics'


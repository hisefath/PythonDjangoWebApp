from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gradeLevel = models.CharField(max_length=100) #Freshmen, Sophomore, Junior, Senior
    major = models.CharField(max_length=100) #ComputerScience, Chemical Engineering, Bio, etc.


    def __str__(self):
        return f'{self.user.username} Profile'
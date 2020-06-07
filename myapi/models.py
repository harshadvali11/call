from django.db import models
from django.contrib.auth.models import User#importing built in user model
# Create your models here.

#creating Profile model to add additional data
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#making relationship b/w 2 models
    PhoneNumber=models.IntegerField(primary_key=True)#declaring number as primary key
    profile_pic=models.ImageField(upload_to='profile_pic/')#profilepic
    def __str__(self):
        return self.user.username
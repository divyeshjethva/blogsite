from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    bio = models.CharField(default="",max_length=255)
    profile = models.ImageField(default="",upload_to='profile/')
    
    def __str__(self):
        return f"{self.name}"
    
class CreateBlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    name =  models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    image = models.ImageField(default="",upload_to='blog/')
    ttime = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return f"{self.name}  |  {self.user}"
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(CreateBlog,on_delete=models.CASCADE)
    ttime = models.DateTimeField(default=timezone.now())
    
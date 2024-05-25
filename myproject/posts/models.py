from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(null=True)
    slug = models.SlugField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    

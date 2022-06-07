from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=65)
    date_added = models.DateTimeField(auto_now_add= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
   
class Entry(models.Model):
    '''Entry for a specific blog post''' 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        '''Return a string representation of the model'''
        return f"{self.text[:50]}...."


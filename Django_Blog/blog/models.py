from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model): 
    host = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=200,default='',blank=True,null=True)
    image = models.FileField(upload_to='media/Blog-images/',default='',blank=True,null=True)
    description = models.TextField(default='',blank=True,null=True)

    def __str__(self):
        return self.name
        
class Comment(models.Model):
    host = models.ForeignKey(User,on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField(default='')

    def __str__(self):
        return self.comment
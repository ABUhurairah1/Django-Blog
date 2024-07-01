from django.db import models

# Create your models here.

class Blog(models.Model): 
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='media/Blog-images/',default=None)
    description = models.TextField()

    def __str__(self):
        return self.name
        

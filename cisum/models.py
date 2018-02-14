from django.db import models

# Create your models here.
class Artist(models.Model):
  text1 = models.CharField(max_length=200)
  

from django.db import models

# Create your models here.
class Biography(models.Model):
    birthdate = models.DateField()
    hometown = models.CharField(max_length=300)
    educational_path = models.TextField()
    discipline = models.CharField(max_length=200)
    compositional_principles = models.TextField()
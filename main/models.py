from django.db import models

# Create your models here.
class Station(models.Model):
	name = models.TextField()
	zone = models.IntegerField()

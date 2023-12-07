from django.db import models

# Create your models here.

class Polls(models.Model):
    name = models.CharField(max_length=5)

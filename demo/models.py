from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=1000)  #first table in the database ie; the original url
    uuid = models.CharField(max_length=10)
from django.db import models

# Create your models here.
class contactus(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=254)
    Number = models.IntegerField()
    Query = models.TextField(max_length=500)
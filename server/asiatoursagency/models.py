from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    number_of_nights = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
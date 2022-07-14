from django.db import models
# from django.contrib.gis.db import models as models

# Create your models here.
class CoffeeShop(models.Model):
    name    = models.CharField(max_length=128)
    address = models.JSONField(max_lenght=2048)
    coordinates = models.JSONField(max_lenght=1024)
    # opening_hours stored in OpenStreetMap opening_hours forman
    opening_hours   = models.CharField(max_length=128, blank=True)
    # photos = 
    # coffee  = models.ManyToManyField(...) 


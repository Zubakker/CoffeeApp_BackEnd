from django.db import models
# from django.contrib.gis.db import models as models

# Create your models here.
class CoffeeShop( models.Model ):
    name    = models.CharField(max_length=128)
    address = models.JSONField(max_lenght=2048)
    coordinates = models.JSONField(max_lenght=1024)
    # opening_hours stored in OpenStreetMap opening_hours format
    opening_hours   = models.CharField(max_length=128, blank=True)


class CoffeeDrink( models.Model ):
    name    = models.CharField(max_length=128)
    parent_shop = models.ForeignKey(
        'CoffeeShop',
        on_delete=models.CASCADE,
    )
    drink_type  = models.CharField(max_length=128)
    description = models.TextField()
    price   = models.FloatField()


class DrinkReview( models.Model ):
    # user = foreignkey

    created = models.DateTimeField(auto_now_add=True)
    quality = models.IntegerField() # from 0 to 10
    # descriptors = foreignkey


from django.contrib import admin

# Register your models here.
from .models import CoffeeShop, CoffeeDrink, DrinkReview, Descriptor

admin.site.register(CoffeeShop)
admin.site.register(CoffeeDrink)
admin.site.register(DrinkReview)
admin.site.register(Descriptor)

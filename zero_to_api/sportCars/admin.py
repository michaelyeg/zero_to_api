from django.contrib import admin

# Register your models here.
from sportCars.models import sportsCar

class sportsCarAdmin(admin.ModelAdmin):
    pass

admin.site.register(sportsCar, sportsCarAdmin)
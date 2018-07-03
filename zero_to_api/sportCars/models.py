from django.db import models

# Create your models here.
class sportsCar(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.BigIntegerField()
    description = models.CharField(max_length=100, default="Michael's sport car")

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.year, self.make, self.model, self.mileage, self.description)
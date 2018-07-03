from rest_framework import serializers
from sportCars.models import sportsCar

class sportsCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = sportsCar
        fields = '__all__'
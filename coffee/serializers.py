from rest_framework import serializers
from .models import Coffee


class CoffeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coffee
        fields = ('name', 'price')

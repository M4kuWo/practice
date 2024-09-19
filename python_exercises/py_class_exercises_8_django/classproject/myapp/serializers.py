from rest_framework import serializers
from .models import Superhero, Creatures

class SuperheroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superhero
        fields = ['id', 'heroname', 'realname', 'medium']

class CreaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creatures
        fields = ['id', 'creaturename', 'origin', 'originname']

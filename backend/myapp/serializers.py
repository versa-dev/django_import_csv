from rest_framework import serializers
from .models import Pokemon

class PokemonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields=['name', 'type_1', 'type_2', 'total', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed', 'generation', 'legendary']
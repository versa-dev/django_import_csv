from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .serializers import PokemonsSerializer
from .models import Pokemon

class PokemonsList(generics.ListCreateAPIView):
  serializer_class = PokemonsSerializer
  queryset = Pokemon.objects.all()

class PokemonFilterByLegendary(generics.ListCreateAPIView):
    serializer_class = PokemonsSerializer
    queryset = Pokemon.objects.filter(legendary=True)
    
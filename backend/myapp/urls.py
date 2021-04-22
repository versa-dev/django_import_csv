from django.urls import path
from .views import PokemonsList, PokemonFilterByLegendary

urlpatterns = [
  path('all/', PokemonsList.as_view()),
  path('filter/', PokemonFilterByLegendary.as_view()),
]
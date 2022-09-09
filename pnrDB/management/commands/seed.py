import requests
from django.core.management.base import BaseCommand
from ...models import PokemonOnRoute, gameRoute,Pokemon,Game,Move,PokemonMove,Trainer
import json

json_data = open('pnrDB\management\commands\data.json') 
data1 = json.load(json_data)
data2 = json.dumps(data1)
json_data.close()


def get_pokemon():
      for i in range(1,600):
        url = 'https://pokeapi.co/api/v2/pokemon/%i' % i 
        r = requests.get(url)
        response = r.json()
        form = response['forms'][0]
        photo = response['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        pokemon = Pokemon(
        name = form['name'],
        sprite = photo
        )   
        pokemon.save()

def get_routes():
    url = 'https://pokeapi.co/api/v2/region/5/'
    r = requests.get(url)
    response = r.json()
    locations = response['locations']
    for place in locations:
      thisRoute = gameRoute(
       gameId = (Game.objects.filter(id=1).first()),
        name = place['name']
      )
      thisRoute.save()

def get_moves():
   for i in range(1,630):
    url = 'https://pokeapi.co/api/v2/move/i' % i 
    r = requests.get(url)
    res = r.json()
    move = Move(
      name = res['names'][7]['name']
    )
    move.save()

def seed_trainerTeam():
    for data in data1:
      pokemonMove = PokemonMove(
      name  = data['name'],
      level = data['level'],
      pokemonId = Pokemon.objects.filter(name =data['pokemonId']['name']).first(),
      moveId = Move.objects.filter(name = data['moveId']['name']).first(),
      trainerId = Trainer.objects.filter(name = data['trainerId']['name']).first(),
      routeId =  gameRoute.objects.filter(name = data['routeId']['name']).first()
      )
      print(pokemonMove)

def seed_encounters():
  pokemons = ['Unown']
  for pokemon in pokemons:
    newPokemon = pokemon.replace(pokemon[0],pokemon[0].lower())
    encounter = PokemonOnRoute(
      name = "Static Volcarona",
      pokemonId = Pokemon.objects.filter(name = newPokemon).first(),
      routeId = gameRoute.objects.filter(pk = 	502).first()
    )
    encounter.save()
class Command(BaseCommand):
  def handle(self, *args, **options):
    get_pokemon()
    get_routes()
    get_moves()
    # seed_trainerTeam()
    # seed_encounters()
    print("completed")
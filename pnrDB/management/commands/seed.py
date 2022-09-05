import requests
from django.core.management.base import BaseCommand
from ...models import PokemonOnRoute, gameRoute,Pokemon,Game,Move,PokemonMove,Trainer



def get_pokemon():
        url = 'https://pokeapi.co/api/v2/pokemon/20' 
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
    url = 'https://pokeapi.co/api/v2/move/250' 
    r = requests.get(url)
    res = r.json()
    move = Move(
      name = res['names'][7]['name']
    )
    move.save()

def seed_trainerTeam():
  moves = ['Draco Meteor','Extreme Speed','Flamethrower','Air Slash']
  for move in moves:
    pokemonMove = PokemonMove(
      name  = "Team Plasma Ghetsis",
      level = 100,
      pokemonId = Pokemon.objects.filter(name ="rayquaza").first(),
      moveId = Move.objects.filter(name = move).first(),
      trainerId = Trainer.objects.filter(name = 'Team Plasma Ghetsis').first(),
      routeId =  gameRoute.objects.filter(pk = 	529).first()
    )
    pokemonMove.save()

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
    # get_pokemon()
    # get_routes()
    # get_moves()
    # seed_trainerTeam()
    seed_encounters()
    print("completed")
import requests
from django.core.management.base import BaseCommand
from ...models import gameRoute,Pokemon,Game,Move



def get_pokemon():
    for i in range(281,650):
        url = 'https://pokeapi.co/api/v2/pokemon/%s' % i
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
  for i in range(251,600):
    url = 'https://pokeapi.co/api/v2/move/%s' % i
    r = requests.get(url)
    res = r.json()
    move = Move(
      name = res['names'][7]['name']
    )
    move.save()


class Command(BaseCommand):
  def handle(self, *args, **options):
    # get_pokemon()
    # get_routes()
    get_moves()
    print("completed")
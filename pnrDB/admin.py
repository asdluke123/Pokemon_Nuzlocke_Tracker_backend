# Register your models here.

from django.contrib import admin
from .models import BoxPokemon, Pokemon,Game,Run,Move,Trainer,gameRoute,User,PokemonMove,PokemonOnRoute

admin.site.register(Pokemon)
admin.site.register(Game)
admin.site.register(Run)
admin.site.register(Move)
admin.site.register(Trainer)
admin.site.register(gameRoute)
admin.site.register(User)
admin.site.register(PokemonMove)
admin.site.register(PokemonOnRoute)
admin.site.register(BoxPokemon)
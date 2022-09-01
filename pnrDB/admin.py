# Register your models here.

from django.contrib import admin
from .models import Pokemon,Game,Run,Move,Trainer,gameRoute,User,PokemonMove

admin.site.register(Pokemon)
admin.site.register(Game)
admin.site.register(Run)
admin.site.register(Move)
admin.site.register(Trainer)
admin.site.register(gameRoute)
admin.site.register(User)
admin.site.register(PokemonMove)
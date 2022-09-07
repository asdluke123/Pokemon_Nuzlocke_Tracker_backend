
from urllib import request
from rest_framework import serializers
from .models import Pokemon,Run,Game,PokemonOnRoute,PokemonMove,Trainer,BoxPokemon,gameRoute,Move,User

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id','name','sprite')
class UserSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','name')
class GameSerialzer(serializers.HyperlinkedModelSerializer):
    userId = UserSerialzer(
        read_only=True
    )
    class Meta:
        model = Game
        fields = ('id','name','photo','userId')
class RunSerialzer(serializers.HyperlinkedModelSerializer):
    
    gameId = GameSerialzer(
        read_only = True
    )
    userId = UserSerialzer(
        read_only = True  
    )
    class Meta:
        model = Run
        fields=('id','name','isComplete','deaths','badges','userId','gameId')
class CreateRunSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('name','userId','gameId')

class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ('id','name')
class TrainerSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('id','name')
class gameRouteSerialzer(serializers.HyperlinkedModelSerializer):
    gameId = GameSerialzer(
        read_only = True
    )
    class Meta:
        model = gameRoute
        fields = ('id','name','gameId')
class PokemonOnRouteSerialzer(serializers.HyperlinkedModelSerializer):
        pokemonId = PokemonSerializer(
            read_only= True
        )
        routeId = gameRouteSerialzer(
            read_only=True
        )
        class Meta:
            model = PokemonOnRoute
            fields = ('id','name','pokemonId','routeId')

class PokemonMoveSerialzer(serializers.HyperlinkedModelSerializer):
        pokemonId = PokemonSerializer(
            read_only= True
        )
        routeId = gameRouteSerialzer(
            read_only=True
        )
        moveId = MoveSerializer(
            read_only=True
        )
        trainerId = TrainerSerialzer(
            read_only=True
        )
        class Meta:
            model = PokemonMove
            fields = ('id','name','pokemonId','moveId','trainerId','routeId','level')

class BoxPokemonSerailzer(serializers.HyperlinkedModelSerializer):
    pokemonId = PokemonSerializer(
        read_only = True
    )
    runId = RunSerialzer(
        read_only = True
    )
    class Meta:
        model = BoxPokemon
        fields = ('id','name','pokemonId','runId')

class CreateBoxPokemonSerailzer(serializers.ModelSerializer):
    class Meta:
        model = BoxPokemon
        fields = ('pokemonId','runId')
    
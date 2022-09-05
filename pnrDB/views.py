from urllib.request import Request
from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import PokemonMoveSerialzer,PokemonSerializer,BoxPokemonSerailzer,TrainerSerialzer,gameRouteSerialzer,RunSerialzer,UserSerialzer,MoveSerializer,GameSerialzer,PokemonOnRouteSerialzer,CreateRunSerialzer,CreateBoxPokemonSerailzer
from .models import Game, Pokemon,PokemonOnRoute,PokemonMove,BoxPokemon,User,Trainer,Move,Run,gameRoute
# Create your views here.

class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
class MoveList(generics.ListCreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
class MoveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class RouteList(generics.ListCreateAPIView):
    queryset = gameRoute.objects.all()
    serializer_class = gameRouteSerialzer
class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = gameRoute.objects.all()
    serializer_class = gameRouteSerialzer

class TrainerList(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerialzer
class TrainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerialzer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
class RunList(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerialzer
class RunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerialzer    
class CreateRunView(APIView):
    serializer_class = CreateRunSerialzer 
    def post(self,request,format =None):
        serialzer = self.serializer_class(data=request.data)
        if serialzer.is_valid():
            user = User.objects.filter(pk = serialzer.data['userId']).first()
            game = Game.objects.filter(pk = serialzer.data['gameId']).first()
            newName = serialzer.data['name']
            newRun = Run(name=newName,userId = user, gameId = game)
            newRun.save()
            return Response(RunSerialzer(newRun).data,status= status.HTTP_200_OK)
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerialzer
class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerialzer

class PokemonMoveList(generics.ListCreateAPIView):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerialzer

class BoxPokemonList(generics.ListCreateAPIView):
    def get(self,request,format = None):
        queryset = (BoxPokemon.objects.filter(runId =request.query_params['route']).first())
        return Response(BoxPokemonSerailzer(queryset).data,status= status.HTTP_200_OK)

class CreateBoxPokemon(APIView):
    serializer_class = CreateBoxPokemonSerailzer
    def post(self,request,format =None):
        serialzer = self.serializer_class(data=request.data)
        if serialzer.is_valid():
            pokemon = Pokemon.objects.filter(pk = serialzer.data['pokemonId']).first()
            run = Run.objects.filter(pk = serialzer.data['runId']).first()
            name = pokemon.name
            newBox = BoxPokemon(name = name,pokemonId = pokemon, runId = run)
            newBox.save()
            return Response(BoxPokemonSerailzer(newBox).data,status= status.HTTP_200_OK)
class PokemonOnRouteList(generics.ListCreateAPIView):
    queryset = PokemonOnRoute.objects.all()
    serializer_class = PokemonOnRouteSerialzer

from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Run(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE, related_name='runs')
    name = models.CharField(max_length=30)
    isComplete = models.BooleanField(default=False)
    deaths = models.IntegerField()
    badges = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    VINTAGEWHITE = 'Vintage White'
    FIRERED = 'Fire Red'
    GAME_CHOICES = [
        (VINTAGEWHITE, 'Vintage White'),
        (FIRERED, 'Fire Red')
    ]
    runId = models.ForeignKey(Run,on_delete=models.CASCADE, related_name='game')
    name = models.CharField(max_length=30, choices=GAME_CHOICES,default=VINTAGEWHITE)
    photo = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class gameRoute(models.Model):
    gameId = models.ForeignKey(Game,on_delete=models.CASCADE,related_name='routes',default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprite = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Move(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PokemonMove(models.Model):
    name = models.CharField(max_length=1000,default='TrainerName PokemonName MoveName RouteName')
    pokemonId= models.ForeignKey(Pokemon,on_delete=models.CASCADE,related_name='pokemon')
    moveId = models.ForeignKey(Move,on_delete=models.CASCADE,related_name='move')
    trainerId = models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name='trainer',default='')
    routeId = models.ForeignKey(gameRoute,on_delete=models.CASCADE,related_name='route',default='')
    def __str__(self):
        return self.name

class PokemonOnRoute(models.Model):
    name = models.CharField(max_length=100, default='')
    pokemonId = models.ForeignKey(Pokemon,on_delete=models.CASCADE,related_name='routePokemon')
    routeId = models.ForeignKey(gameRoute,on_delete=models.CASCADE,related_name='pokemonRoute')

    def __str__(self):
        return self.name

class BoxPokemon(models.Model):
    name = models.CharField(max_length=100,default='')
    pokemoId = models.ForeignKey(Pokemon, on_delete=models.CASCADE,related_name='boxPokemomn')
    runId = models.ForeignKey(Run,on_delete=models.CASCADE,related_name='boxRun')

    def __str__(self):
        return self.name
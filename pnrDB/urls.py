from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('pokemon/',views.PokemonList.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>',views.PokemonDetail.as_view(), name='pokemon-detail'),

    path('move/',views.MoveList.as_view(),name='move-list'),
    path('move/<int:pk>',views.MoveDetail.as_view(), name='move-detail'),
    
    path('route/',views.RouteList.as_view(),name='route-list'),
    path('route/<int:pk>',views.RouteDetail.as_view(), name='route-detail'),
    
    path('trainer/',views.TrainerList.as_view(),name='trainer-list'),
    path('trainer/<int:pk>',views.TrainerDetail.as_view(), name='trainer-detail'),

    path('user/',views.UserList.as_view(),name='user-list'),
    path('user/<int:pk>',views.UserDetail.as_view(), name='user-detail'),

    path('run/',views.RunList.as_view(),name='run-list'),
    path('run/<int:pk>', views.RunDetail.as_view(),name='run-detail'),
    path('createrun/',views.CreateRunView.as_view(),name='create-run'),
    
    path('game/',views.GameList.as_view(), name='game-list'),
    path('game/<int:pk>',views.GameDetail.as_view(),name='game-detail'),

    path('trainerteam/',views.PokemonMoveList.as_view(), name='trainerteam-list'),

    path('boxpokemon/',views.BoxPokemonList.as_view(), name='boxpokemon-list'),

    path('routepokemon/',views.PokemonOnRouteList.as_view(), name='routepokemon-list')

]